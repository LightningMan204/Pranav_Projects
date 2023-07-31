import datetime as dt
import time as t

def time():
    timelogged = dt.datetime.now().strftime("%H:%M:%M")
    print("You started this today at " + timelogged)

def calc():
    print("Booting up the calculator")
    t.sleep(5)
    print("done now start")
    t.sleep(1)

time()
calc()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
