import pygame
import random

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
paddle_speed = 5

# Set the ball properties
ball_width = 10
ball_height = 10
ball_speed_x = 3
ball_speed_y = 3

# Initialize the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Create paddles
paddle1 = pygame.Rect(50, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle2 = pygame.Rect(screen_width - 50 - paddle_width, screen_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(screen_width // 2 - ball_width // 2, screen_height // 2 - ball_height // 2, ball_width, ball_height)

# Set initial ball direction
ball_direction = random.choice([-1, 1]), random.choice([-1, 1])

# Set the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Move the paddles
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.y < screen_height - paddle_height:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.y < screen_height - paddle_height:
        paddle2.y += paddle_speed

    # Move the ball
    ball.x += ball_speed_x * ball_direction[0]
    ball.y += ball_speed_y * ball_direction[1]

    # Check collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Check collision with walls
    if ball.y <= 0 or ball.y >= screen_height - ball_height:
        ball_direction = ball_direction[0], -ball_direction[1]

    # Check if the ball is out of bounds
    if ball.x <= 0 or ball.x >= screen_width - ball_width:
        # Reset the ball position
        ball.x = screen_width // 2 - ball_width // 2
        ball.y = screen_height // 2 - ball_height // 2

        # Randomize the ball direction
        ball_direction = random.choice([-1, 1]), random.choice([-1, 1])

    # Clear the screen
    screen.fill(black)

    # Draw paddles
    pygame.draw.rect(screen, white, paddle1)
    pygame.draw.rect(screen, white, paddle2)

    # Draw the ball
    pygame.draw.ellipse(screen, white, ball)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

