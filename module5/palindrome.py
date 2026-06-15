"""Write a program that checks whether a given word is a palindrome (reads the same 
forwards and backwards), ignoring case and spaces (e.g., 'Madam' and 'nurses run'). """
n = input("Enter the string to check if it's a palindrome: ")
if n == n[::-1]:
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
