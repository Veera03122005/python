"""Write a program that takes a sentence as input and prints: 
the number of characters, the 
number of words, the sentence in uppercase, and the sentence reversed."""
s = input("Enter a sentence: ")
char_count = len(s)
word_count = len(s.split())
uppercase = s.upper()
reversed_string = s[::-1]
print("************************************")
print(f"The sentence you entered is: {s}")
print(f"Number of characters:        {char_count}")
print(f"Number of words:             {word_count}")
print(f"Sentence in uppercase:       {uppercase}")
print(f"Sentence reversed:           {reversed_string}")
print("****************************************")
