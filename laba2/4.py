x = 8
y = 8

print("Введіть координати ферзя (x,y): ")
xQ = int(input())
yQ = int(input())

if (xQ > x or yQ > y):
    print("Ви не можете вийти за межі поля!")

print("Введіть координати тури (x,y): ")
xR = int(input())
yR = int(input())

if (xR > x or yR > y):
    print("Ви не можете вийти за межі поля!")

print("Введіть координати коня (x,y): ")
xH = int(input())
yH = int(input())

if (xH > x or yH > y):
    print("Ви не можете вийти за межі поля!")

if (xQ == xR and yQ == yR):
    print("Помилка, фігури не можуть бути в одній клітинці!")

if (xQ == xH and yQ == yH):
    print("Помилка, фігури не можуть бути в одній клітинці!")

if (xR == xH and yR == yH):
    print("Помилка, фігури не можуть бути в одній клітинці!")

# Захист
if ((xR == xQ and yR != yQ) or (xR != xQ and yR == yQ)):  #Захист ферзя турою
    print("Тура захищає ферзя!")
if ((xQ == xR and yQ != yR) or (xQ != xR and yQ == yR)): #Захист тури ферзем
    print("Ферзь захищає туру!")
elif (abs(xQ - yQ) == abs(xR - yR)):
    print("Ферзь захищає туру!")


if ((xR == xH and yR != yH) or (xR != xH and yR == yH)): #Чекаємо туру і коня
    print("Тура нападає на коня!")

if ((xH - xQ == 2 or xH - xQ == -2) and ((yH - yQ == 1 or yH - yQ == -1))): #Логіка коня
    print("Кінь напарає на ферзя!")

if ((yH - yQ == 2 or yH - yQ == -2) and ((xH - xQ == 1 or xH - xQ == -1))):
    print("Кінь напарає на ферзя!")

if ((xH - xR == 2 or xH - xR == -2) and ((yH - yR == 1 or yH - yR == -1))):
    print("Кінь напарає на туру!")

if ((yH - yR == 2 or yH - yR == -2) and ((xH - xR == 1 or xH - xR == -1))):
    print("Кінь напарає на туру!")

if ((xQ == xH and yQ != yH) or (xQ != xH and yQ == yH)): # Чекаємо ферзя і коня
    print("Ферзь нападає на коня!")
elif (abs(xQ - yQ) == abs(xH - yH)):
    print("Ферзь нападає на коня!")






