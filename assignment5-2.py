class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x 
calculator = Calculator()
while True:
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = calculator.add(x, y)
        elif operation == '-':
            result = calculator.subtract(x, y)
        elif operation == '*':
            result = calculator.multiply(x, y)
        elif operation == '/':
            result = calculator.divide(x, y)
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice != 'yes':
        break