from math import sqrt

print("Введіть точність: ")
eps = float(input())

sum = 0
subSum = 0
element = 1

x = 1

while x <= 5:
    k = 0
    subSum = 0
    element = 1
    while abs(element) > eps:
        if ((pow(-1,k) * pow(x,k)) / (pow((k + 2),3) + sqrt(k))) > max(float):
            element = (pow(-1,k) * pow(x,k)) / (pow((k + 2), 3) + sqrt(k))
            if element + subSum < max(float):
                subSum += element
            else:
                break
    k += 1

if sum + subSum < eps or sum + subSum >= eps:
    sum += subSum

x += 1


print("Сума = " + sum)


