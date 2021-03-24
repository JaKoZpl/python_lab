import re

# aaa sss vvvvv ff structure ads structure

string = input("Введіть рядок: ")

file1 = open("file_1.txt", "w")
file1.write(string)
file1.close()

file1 = open("file_1.txt")
stringFinal = file1.read()
file1.close()

pattern = r"\W"
words = re.split(pattern, stringFinal)
print(words)

count = 0
for i in words:
    if "structure" == i:
        count += 1

print(count)

index = 0
indexCount = 0
temp = ""
for i in stringFinal:
    if i == "s":
        index = indexCount
    if i == " ":
        if temp.strip() == "structure":
            break
        else:
            temp = ""
    temp += i
    indexCount += 1

print(index)
file2 = open("file_2.txt", "w")
file2.write("кількість повторень = " + str(count) + ", номер символу = " + str(index))
file2.close()