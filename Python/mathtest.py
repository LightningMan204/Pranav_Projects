import random

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '/':
        # Ensure the division has a whole number result
        num2 = random.randint(1, 10)
        num1 = num2 * random.randint(1, 10)
    
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def main():
    print("Welcome to the Math Test!")
    print("You will be given 100 random arithmetic questions.")
    print("Type 'exit' to finish the test.")

    correct_answers = 0
    for i in range(1, 101):
        question, correct_answer = generate_question()
        user_answer = input(f"Question {i}: {question} = ")
        
        if user_answer.lower() == 'exit':
            break

        try:
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                correct_answers += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct answer was: {correct_answer}")
        except ValueError:
            print("Invalid input. Please enter a number or type 'exit' to finish the test.")

    print(f"\nTest completed!\nYou answered {correct_answers} out of 100 questions correctly.")

if __name__ == "__main__":
    main()

