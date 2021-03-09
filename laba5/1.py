
# Номер 1
print("Введіть розмірність масиву: ")
size = int(input())
i = 0

list = []
final_list = []

print("Введіть елементи масиву: ")
while i < size:
    i += 1
    list.append(input())
print("Початковий масив: " + str(list))

for item in list[::2]:
    final_list += item
print("Фінальний масив: " + str(final_list))

# Номер 2
print("Введіть розмірність масиву: ")
size = int(input())
arr = []
print("Введіть елементи масиву:")
while size:
    arr.append(int(input()))
    size = size - 1

print("Початковий список: " + str(arr))
print("Фінальний список: " + str([item for item in arr[::2]]))

