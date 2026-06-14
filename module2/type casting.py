"""
Write a program that takes two numbers entered as strings (e.g., num1 = "15", num2 =
"4"), converts them to integers, and prints their sum, difference, product and quotient.
"""
num1 = "15"
num2 = "4"
print(int(num1)+int(num2))
print(int(num1)-int(num2))
print(int(num1)*int(num2))
print(int(num1)/int(num2))
"""
Predict and then verify the output of: print(10 / 3), print(10 // 3), print(int(10/3)),
print(float(10)). Write down why each result looks the way it does.
Type casting techniques
"""
print(10 / 3)  # This output 3.3333333333333335 because the division operator (/) returns a float value.
# This output 3 because the floor division operator (//) returns the largest integer less than or equal to the division result.
print(10 // 3)
print(int(10 / 3))  # This output 3 because the int() function
# This output 10.0 because the float() function converts the integer 10 to a float value.
print(float(10))
# Implicit and explicit type conversion
a = 5
b = 10.5
# Implicit type conversion
c = a+b
# This output 15.5 because the integer 5 is implicitly converted to a float before the addition operation.
print(c, type(c))
# Explicit type conversion
d = int(b)
# This output 10 because the float 10.5 is explicitly converted to an integer using the int() function, which truncates the decimal part.
print(d, type(d))
