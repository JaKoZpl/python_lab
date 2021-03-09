print("Введіть x (дісьне число): ")
x = float(input())
print("Введіть y (дісьне число): ")
y = float(input())

def sum_two_digits(x, y):
    return pow(x, 2) + pow(y, 2)

print(sum_two_digits(x, y))
