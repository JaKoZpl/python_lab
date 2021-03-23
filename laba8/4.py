import re


def check_word(oldWord):
    array = list(oldWord)
    alf = True
    temp = array[0]
    for j in range(1, len(oldWord), 1):
        if re.match("[ ,.!?;:-]", str(array[j])):
            break
        if temp <= array[j]:
            alf = True
            temp = array[j]
        else:
            alf = False
            break

    if alf:
        return ""
    else:
        return oldWord


text = input("Введіть текст: ")
words = text.split(" ")

for i in range(len(words)):
    words[i] = check_word(words[i])

print(*words)