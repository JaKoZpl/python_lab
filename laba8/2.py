import string

a = "Я дуже love python"

final = " "
lst = a.split()
sp = (string.ascii_lowercase + string.ascii_uppercase + " ")
for i in a:
    if i in sp:
        final += i

stroka = final.split()
print(stroka)
print("Кількість: " + str(len(stroka)))
delet = int(input("Яке бажеєте видалити? "))
stroka.pop(delet)
print(stroka)
invite = input("Введіть слово яке бажаєте добавити: ")
stroka.append(invite)
print(stroka)
