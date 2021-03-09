print("Введіть a: ")
a = int(input())


def sum_of_digits(x):
    i = 1
    final = 0
    while i <= 10:
        final += (expt(x, i) / i)
        i += 1
    return final


def expt(digit, n):
    if n == 0:
        return 1
    return digit * expt(digit, n-1)


print((3 * sum_of_digits(a / 2) + 5 * sum_of_digits(expt(a, 2) - 2)))