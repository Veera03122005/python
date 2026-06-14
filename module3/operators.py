""" Write a program that takes two numbers and prints the results of all arithmetic 
operators (+, -, *, /, //, %, **) applied to them, with clear labels. """
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum of {a} and {b} is: {a+b}")
print(f"Difference of {a} and {b} is: {a-b}")
print(f"Product of {a} and {b} is: {a*b}")
print(f"Quotient of {a} and {b} is: {a/b}")
print(f"Floor Division of {a} and {b} is: {a//b}")
print(f"Modulus of {a} and {b} is: {a % b}")
print(f"Exponentiation of {a} and {b} is: {a**b}")
