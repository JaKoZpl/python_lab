import math

print("Введіть значення Y,Z: ")
y = float(input())
z = float(input())
print("Введіть значення x: ")
x = float(input())

if (x >= y):
    f = ((pow(x,2) + pow(math.e,2)) / math.cos(y))
    print(f)
else: print(math.sin(x) + math.cos(z))
