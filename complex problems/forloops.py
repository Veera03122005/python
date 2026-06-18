# forloop example1
# from 0 to 10
for i in range(0, 11, 1):
    print(i)
print("******************X******************")
# from 20 to 0 with step -2
for i in range(20, 0, -2):
    print(i)
print("******************X******************")
# from 50 to 0 with step -5
for i in range(50, 0, -5):
    print(i)
print("******************X******************")
for i in range(1, 11, 1):
    print(i*i*i)
total = 0
for i in range(1, 11, 1):
    total += i
print(total)
print("****************X******************")
