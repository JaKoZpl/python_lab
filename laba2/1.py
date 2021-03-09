print("Введіть значення x,y для точки: ")
x = int(input())
y = int(input())

if (pow(-x,2) + 2 >= y):
    if (x == y):
        print("На межі!")
    elif (x >= 0 & y >= 0):
        if (x < y):
            if ((pow(-x,2) + 2 == y)):
                print("На межі!")
            else: (print("Так!"))
        elif (x > y):
            if ((pow(-x,2) + 2 == y)):
                print("На межі!")
            else: (print("Так!"))
        else: print("Ні!")

    elif (x <= 0 & y <= 0):
        if (x > y):
            if (pow(-x,2) + 2 == y):
                print("На межі!")
            else: print("Так!")

        elif (x < y):
            if (pow(-x,2) + 2 == y):
                print("На межі!")
            else: print("Так!")
        else: print("Ні!")
    else: print("Ні!")

else: print("Ні!")