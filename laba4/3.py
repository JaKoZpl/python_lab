print("Введіть кількість чисел: ")
x = int(input())

def sum_of_range(m: int) -> int:
    sum_of_digits = 0
    for digit in range(m + 1):
        if digit > 5:
            sum_of_digits = sum_of_digits + digit
    return sum_of_digits


print(sum_of_range(x))


def sum_of_range2(m: int) -> int:
    return sum(range(6, m + 1))


print(sum_of_range2(x))
