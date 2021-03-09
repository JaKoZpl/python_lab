import random

size_r = int(input("Введіть кількість рядків: "))
size_c = int(input("Введіть кількість стовпців: "))

matrix = [[random.randint(0, 10)for j in range(size_c)] for i in range(size_r)]

for item in matrix:
    for number in item:
        print("{:^3d}".format(number), end=" ")
    print()

count = 0
suma = 0
print()
for item in matrix:
    for number in item:
        if number % 2 == 0:
            count += 1
            suma += number
print("Кількість:", count)
print("Сума:", suma / count)