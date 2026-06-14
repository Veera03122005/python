"""Given an integer entered by the user, write a program that checks and prints whether 
the number is even or odd, and whether it is positive, negative, or zero - using 
comparison and logical operators."""
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
# Check positive, negative, or zero
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
