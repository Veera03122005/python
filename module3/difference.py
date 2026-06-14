"""Write a program that demonstrates the difference between 
'==' and 'is' using two lists 
that contain the same elements but are created separately."""
lst1 = [1, 3, 5, 7, 9]
lst2 = [1, 3, 5, 7, 9]
print(lst1, type(lst1))
print(lst2, type(lst2))
if lst1 == lst2:
    print("Both lists are equal")
else:
    print("Both lists are not equal")

if lst1 is lst2:
    print("Both lists are same")
else:
    print("Both lists are not same")
