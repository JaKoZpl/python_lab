text = open("info.txt", "w")
finalText = open("final.txt", "w")

while True:
    try:
        a = int(input("Введіть значення a: "))
        b = int(input("Введіть значення b: "))
        arithmetic = input("Введіть дію: ")

        text.write(str(a) + " " + arithmetic + " " + str(b) + "\n")


        arithmeticOperations = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b
        }

        finallRez = arithmeticOperations[arithmetic]
        print("Результат: " + str(finallRez))

        finalText.write("Ваш вираз: " + str(a) + arithmetic + str(b) + " Результат: " + str(finallRez) + "\n")

        exit = input("Якщо бажаєте закінчити роботу введіть 'exit': ")
        if exit == "exit":
            break
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
    except KeyError:
        print("Не коректно введена дія!")

finalText.close()
text.close()