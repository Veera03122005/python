"""Without running the code, evaluate the expression:
 10 + 2 * 3 ** 2 - (8 / 4). Then write a program to verify your manual calculation and explain any difference using operator precedence rules.
"""
"""To evaluate the expression `10 + 2 * 3 ** 2 - (8 / 4)` 
    manually, we need to follow the order of operations, also known as operator precedence. 
The order of operations is as follows:
1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication `*` and Division `/` (from left to right)
4. Addition `+` and Subtraction `-` (from left to right)
"""
# python program
Expression = 10 + 2 * 3 ** 2 - (8 / 4)
print("The result of the expression 10 + 2 * 3 ** 2 - (8 / 4) is:", Expression)
