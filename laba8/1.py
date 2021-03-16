# 1
country = input("Введіть назву держави: ")
president = input("Введіть прізвище президента: ")
print(president + " є президентом держави " + country)

# 2
namber1 = input("Введіть рядок номер 1: ")
namber2 = input("Введіть рядок номер 2: ")
ar1 = []
ar2 = []
for i in namber1:
    ar1 += i
for i in namber2:
    ar2 += i
final = [ar1[-2:] + ar2[:2]]

line = ""
for item in final:
    for j in item:
        line += j
print("Наш рядок: " + line)

# 3
name = "антикваріат"
cons = "варіант"
n1 = []
for item in name:
    n1 += item
print(n1[5:10] + n1[1:2] + n1[10:])

# 4
str = input("Введіть рядок (txt, html): ")
print(str.replace("txt", "html"))