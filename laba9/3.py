text = open("info.txt")
finalText = open("final.txt", "w")

while True:
    try:
        a = 0
        b = 0
        operator = ""

        OpL = ["+", "-", "/", "*"]

        file_content = text.read()
        for i in file_content:
            if i in OpL:
                operator = i
                file_content = file_content.split(i)

        a = int(file_content[0])
        b = int(file_content[1].strip())

        print("Для завершення роботи введіть exit: ")

        arithmeticOperations = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b
        }

        finallRez = arithmeticOperations[operator]

        finalText.write("Ваш вираз: " + str(a) + operator + str(b) + " Результат: " + str(finallRez) + "\n")
        print(a)
        print(b)
        print(operator)

        exit = input()
        if exit == "exit":
            break
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
    except KeyError:
        print("Не коректно введена дія!")

finalText.close()
text.close()


# Вхідний файл:
# 2
# 3
# operatisa = input("Введіть операцію: ")
# a + operatisa + b
