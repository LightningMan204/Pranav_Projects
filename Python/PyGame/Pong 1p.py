import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 400

# Set the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set the paddle properties
paddle_width = 10
paddle_height = 60
paddle_velocity = 5

# Set the ball properties
ball_radius = 10
ball_velocity_x = 3
ball_velocity_y = 3

# Set the score properties
score_font = pygame.font.Font(None, 36)
player_score = 0
opponent_score = 0

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Create the paddles
player_paddle = pygame.Rect(50, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(screen_width // 2 - ball_radius // 2, screen_height // 2 - ball_radius // 2, ball_radius, ball_radius)
ball_velocity = [ball_velocity_x, ball_velocity_y]

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the player paddle
    if keys[pygame.K_w] and player_paddle.y > 0:
        player_paddle.y -= paddle_velocity
    if keys[pygame.K_s] and player_paddle.y < screen_height - paddle_height:
        player_paddle.y += paddle_velocity

    # Move the opponent paddle
    if opponent_paddle.y < ball.y and opponent_paddle.y < screen_height - paddle_height:
        opponent_paddle.y += paddle_velocity
    if opponent_paddle.y > ball.y and opponent_paddle.y > 0:
        opponent_paddle.y -= paddle_velocity

    # Update the ball position
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Check collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_velocity[0] = -ball_velocity[0]

    # Check collision with walls
    if ball.y > screen_height - ball_radius or ball.y < 0:
        ball_velocity[1] = -ball_velocity[1]

    # Check if ball goes out of bounds
    if ball.x > screen_width:
        player_score += 1
        ball.x = screen_width // 2 - ball_radius // 2
        ball.y = screen_height // 2 - ball_radius // 2
        ball_velocity[0] = -ball_velocity[0]
    elif ball.x < 0:
        opponent_score += 1
        ball.x = screen_width // 2 - ball_radius // 2
        ball.y = screen_height // 2 - ball_radius // 2
        ball_velocity[0] = -ball_velocity[0]

    # Clear the screen
    screen.fill(black)

    # Draw the paddles
    pygame.draw.rect(screen, white, player_paddle)
    pygame.draw.rect(screen, white, opponent_paddle)

    # Draw the ball
    pygame.draw.ellipse(screen, white, ball)

    # Draw the score
    score_text = score_font.render(f"{player_score} : {opponent_score}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
