import random

size = int(input("Введіть розмір: "))

matrix = [[random.randint(0, 100) for j in range(size)] for i in range(size)]

for item in matrix:
    for number in item:
        print("{:^3d}".format(number), end=" ")
    print()

arr_b = [sum(i) / len(i) for i in matrix]

print()
print(arr_b)