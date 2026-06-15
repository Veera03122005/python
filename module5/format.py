"""Write a program that takes a full name as input (e.g., ' john Michael smith ') and prints it 
neatly formatted as 'John Michael Smith' with extra spaces removed and each word 
capitalized. """
name = input("Enter your full name: ")
formatted_name = name.strip().title()
print(f"Formatted name: {formatted_name}")
