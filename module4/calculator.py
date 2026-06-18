"""2. Write a 'Simple Calculator' program that takes two numbers and an operator (+, -, *, /) 
as input and prints the result formatted to 2 decimal places."""
while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print(f"Addition of {num1} and {num2} is: {num1 + num2:.2f}")

    elif operator == "-":
        print(f"Subtraction of {num1} and {num2} is: {num1 - num2:.2f}")

    elif operator == "*":
        print(f"Multiplication of {num1} and {num2} is: {num1 * num2:.2f}")

    elif operator == "/":
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(f"Division of {num1} and {num2} is: {num1 / num2:.2f}")

    else:
        print("Invalid operator. Please enter one of +, -, *, /.")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Calculator closed.")
        break