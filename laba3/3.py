print("Номер пострілу / Координати пострілу / Результат")
s = 0
n = 0
final = ""

while s < 10:
    s += 1
    n += 1

    print("Введіть значення x,y для точки: ")
    x = int(input())
    y = int(input())

    if (pow(-x, 2) + 2 >= y):
        if (x == y):
            final = "Потрапив у мішень!"
        elif (x >= 0 & y >= 0):
            if (x > y):
                if ((pow(-x, 2) + 2 == y)):
                    final = "Потрапив у мішень!"
                else:
                    final = "Потрапив у мішень!"
            else:
                final = "Мішень не ушкоджена!"
        elif (x <= 0 & y <= 0):
            if (x < y):
                if (pow(-x, 2) + 2 == y):
                    final = "Потрапив у мішень!"
                else:
                    final = "Потрапив у мішень!"
            else:
                final = "Мішень не ушкоджена!"
        else:
            final = "Мішень не ушкоджена!"
    else:
        final = "Мішень не ушкоджена!"

    print(str(n) + ")" + " x = " + str(x) + " y = " + str(y) + " Результат: " + final)




