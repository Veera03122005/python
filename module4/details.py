"""Write a program that asks the user for their name, college, and year of graduation, then 
prints a formatted welcome message using an f-string."""
name = input("Enter your name: ")
college_name = input("Enter your college name: ")
graduation_year = int(input("Enter your year of graduation: "))
print(
    f"Welcome, {name}! You are a student of {college_name} and will graduate in {graduation_year}.")
