import re

# file1 = open("TF_1", "w")
# file2 = open("TF_2", "w")

# print(len(file1.read()))


# file1.close()
# file2.close()

file1 = open("TF_1")
allContent = file1.read()
file1.close()

pattern = r"\W"
words = re.split(pattern, allContent)
print(words)
maxLen = 0
for word in words:
    if len(word) > maxLen:
        maxLen = len(word)

finalList = []
for i in words:
    if len(i) == maxLen:
        finalList.append(i)

print(maxLen)
print(finalList)

file2 = open("TF_2", "w")

count = 0
for i in range(len(finalList) // 5 + 1):
    temp = " ".join(finalList[count:count + 5]) + "\n"
    file2.write(temp)
    print(temp)
    count += 5
file2.close()

