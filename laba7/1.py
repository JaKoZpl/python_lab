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

print("Елементи які є в першому масиві, без повторень: ")
list1 = [item for item in set(A) if A.count(item) < 2]
print(list1)
print("Елементи які повторюються в першому масиві (для перевірки): ")
test = [item for item in set(A) if A.count(item) > 1]
print(test)

list2 = [item for item in set(B) if B.count(item) > 1]
print("Елементи які повторюються в другому масиві: ")
print(list2)

c = []
def lin():
    for i in list1:
        for j in list2:
            if i == j:
                c.append(i)
    print(c)

print("Фінальний масив:")
lin()

print()
final = sorted(list1 + list2)
print(final)



# mid = len(final) // 2
# low = 0
# high = len(final) - 1
# for item in c:
#     while final[mid] != item and low <= high:
#         if item > final[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#         mid = (low + high) // 2
#
#     if low > high:
#         print("Чисел немає! ")
#     else:
#         print("ID = ", mid)

