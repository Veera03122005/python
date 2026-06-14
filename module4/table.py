""" Write a program that prints a multiplication table for a number entered by the user, with 
the numbers right-aligned in columns of width 5 (hint: use the :>5 format specifier inside 
an f-string within a loop)."""
n = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication Table for {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i:>2}")
