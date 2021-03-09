import random

arr = []
for i in range(17):
    arr.append(random.randint(-10, 20))

print("Початковий масив:", str(arr))

print("Максимальний елемент:", str(abs(max(arr))))
print("Мінімальний елемент:", str(abs(min(arr))))

print()
maximum = max(arr)
print("Індекс максимальноо елементу:", str(arr.index(maximum)))
minimum = min(arr)
print("Індекс мінімального елементу:", str(arr.index(minimum)))

print()
list = arr[arr.index(maximum) : arr.index(minimum) + 1]
print("Фінальний лист:", str(list))

suma = 0
for item in list:
    suma += abs(item)
print("Сума елементів:", str(suma))
