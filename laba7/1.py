import random


def make_arr() -> list:
    array = []
    while len(array) < 30:
        array.append(random.randint(-49, 50))
    return array


A = make_arr()
B = make_arr()

print("Перший масив:")
print(A)
print("Другий масив:")
print(B)
print()



def binary(array, value, index):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2

        if value == array[middle] and index != middle:
            return True
        if value < array[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return False


def lin(array, value, index):
    for i in range(len(array)):
        if array[i] == value and i != index:
            return i
    return -1


def common_row_method(a, index):
    n = len(a)
    array = []
    for i in range(n):
        array.append([])
        for j in range(n):
            array[i].append(False)

    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == j:
                continue
            if a[i] == a[j]:
                array[i][j] = True

    for i in range(len(array)):
        if array[index][i]:
            return False

    return True

# Виводить ті які є декілька в другому, і унікальні в першому
for i in range(len(A)):
    if not binary(A, A[i], i):
        secondArrayHave = lin(B, A[i], -1)
        if secondArrayHave != -1 and lin(B, A[i], secondArrayHave) != -1:
            print("Фінальний: ", A[i])

# Виводить ті які є декілька в першому, і унікальні в другому
for i in range(len(B)):
    if common_row_method(B, i):
        secondArrayHave = lin(A, B[i], -1)
        if secondArrayHave != -1 and lin(A, B[i], secondArrayHave) != -1:
            print("Фінальний b: ", B[i])

