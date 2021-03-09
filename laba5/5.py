#
# size_r = int(input("Введіть кількість рядів: "))
# size_c = int(input("Введіть кількість місць: "))
#
# matrix = [[int(input())for j in range(size_c)] for i in range(size_r)]
#
# for item in matrix:
#     for number in item:
#         print("{:^3d}".format(number), end=" ")
#     print()
#
# row = int(input("Введіть ряд в якому бажаєте перевірити місця: "))
# print(matrix[row - 1])
#
# sold = 0
# free = 0
# for item in matrix[row - 1]:
#     if item != 1:
#         free += 1
#     else: sold += 1
# print("Вільних місць:", free)
# print("Зайнятих місць:", sold)
#


# Номер 2
size_r = int(input("Введіть кількість рядів: "))
size_c = int(input("Введіть кількість місць: "))

matrix = [[int(input())for j in range(size_c)] for i in range(size_r)]

for item in matrix:
    for number in item:
        print("{:^3d}".format(number), end=" ")
    print()

row = int(input("Введіть ряд в якому бажаєте перевірити місця: "))
print(matrix[row - 1])

chosen_row = matrix[row - 1]
free = len(chosen_row) - sum(chosen_row)
print("Вільних місць:", free)

