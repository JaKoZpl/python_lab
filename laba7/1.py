import random

def make_arr()->list:
    array = []
    while len(array) < 10:
        array.append(random.randint(-49, 50))
    return array

A = make_arr()
B = make_arr()

print("Перший масив:")
print(A)
print("Другий масив:")
print(B)