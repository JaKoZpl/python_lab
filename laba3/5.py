print("Введіть вагу однієї зернини: ")
weight = float(input())

a = 1
s = 0
i = 0
sum = 0

while i < 64:
    i += 1
    s = s + 1
    a = a * 2
    print(str(s) + ")" + " Кількість зерен: " + str(a))
    sum += a * 2

print("Загальна cума зернен: " + str(sum))
print("Загальна вага зерна: " + str(weight * sum))