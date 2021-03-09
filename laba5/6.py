
size_r = int(input("Введіть кількість рядків: "))

matrix = []

for i in range(size_r):
    temp = input("Введіть числа: ").split()
    for j in range(len(temp)):
        temp[j] = int(temp[j])

    matrix.append(temp)


for item in matrix:
    for number in item:
        print("{:^3d}".format(number), end=" ")
    print()

matrix2 = []

print()
for item in matrix:
    if len(item) % 2 == 0:
        matrix2.append([i + 7 for i in item])
    else: matrix2.append([i - 7 for i in item])


for item in matrix2:
    for number in item:
        print("{:^3d}".format(number), end=" ")
    print()