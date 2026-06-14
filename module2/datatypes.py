"""Create variables to store your name (str), age (int), height in metres (float) and whether
 you are a graduate (bool). Print each variable along with its type using type().
"""
name = "Veera Sai"
age = 20
height = 1.85
is_graduate = True
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_graduate, type(is_graduate))


# list and its conversion to tuple, tuple and its conversion to set
lst1 = [1, 2, 3, 4, 5]
print(lst1, type(lst1))
tup2 = tuple(lst1)
print(tup2, type(tup2))
set2 = set(lst1)
print(set2, type(set2))

tup1 = (1, 2, 3, 4, 5)
print(tup1, type(tup1))
set1 = {1, 2, 3, 4, 5}
print(set1, type(set1))
