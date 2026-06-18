""" Write a program that takes three numbers as input and prints the largest of the three
using only if/elif/else statements (without using max())."""
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

if num1 == num2 == num3:
    print("All are equal")
elif num1 >= num2 and num1 >= num3:
    print(f"{num1} is greater Number")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is greater Number")
else:
    print(f"{num3} is greater Number")