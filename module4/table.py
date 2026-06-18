""" Write a program that prints a multiplication table for a number entered by the user, with 
the numbers right-aligned in columns of width 5 (hint: use the :>5 format specifier inside 
an f-string within a loop)."""
while True:
    n = int(input("Enter a number to print its multiplication table: "))

    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

    choice = input("\nDo you want another table? (yes/no): ").lower()

    if choice in ["no"]:
        print("Program ended.")
        break
    elif choice not in ["yes"]:
        print("Invalid choice! Please enter yes/no")