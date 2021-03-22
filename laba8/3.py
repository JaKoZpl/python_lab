import re

sentence = r'Я дуже love cerf _тратата _241 python'
sentence = sentence.split()
print(sentence)
final = [item for item in sentence if item[0] != "_" and not re.search('[a-z A-Z]', item[0])]
print(final)