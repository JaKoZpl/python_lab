import random

def make_arr()->list:
    array = []
    while len(array) < 10:
        array.append(random.randint(-49, 50))
    return array

array1 = make_arr()
array2 = make_arr()
print("Перший масив:")
print(array1)
print("Другий масив:")
print(array2)

# Бульбашкове сортування
def bubble(array)->list:
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print("Сортування першого бульбашкою:")
print(bubble(array1))


# Сортування змішуванням
def cocktail(array)->list:
    left = 0
    right = len(array) - 1

    while left <= right:
        for i in range(left, right, +1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        right -= 1

        for i in range(right, left, - 1):
            if array[i - 1] > array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]
        left += 1

    return(array)

print("Сортування першого змішуванням:")
print(cocktail(array1))

# Сортування включенням
def insertion(array)->list:
    lenght = len(array)
    for item in range(1,lenght):
        key = array[item]
        j = item
        while(j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        array[j] = key
    return array
print("Сортування першого включенням:")
print(insertion(array1))

# Сортування частинами
def stooge(array, i = 0, j = None)->list:
    if j is None:
        j = len(array) - 1
    if array[j] < array[i]:
        array[i], array[j] = array[j], array[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stooge(array, i, j - t)
        stooge(array, i + t, j)
        stooge(array, i, j - t)
    return array

print("Сортування частинами:")
print(stooge(array1))

# Cортування Шелла
def shell(array)->list:
    inc = len(array) // 2
    while inc:
        for i, el in enumerate(array):
            while i >= inc and array[i - inc] > el:
                array[i] = array[i - inc]
                i -= inc
            array[i] = el
        inc = 1 if inc == 2 else int(inc * 5 / 11)
    return array

print("Сортування Шелла:")
print(shell(array2))

# Cортування злиттям
def merge(array)->list:
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        rihgt = array[mid:]

        i, j, k = 0, 0, 0


    while i < len(left) and j < len(rihgt):
        if left[i] < rihgt[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = rihgt[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(rihgt):
        array[k] = rihgt[j]
        j += 1
        k += 1
    return array

print("Cортування злиттям:")
print(merge(array2))

# Cортування вибором
def selection(array)->list:
    for item in range(len(array) - 1):
        m = item
        j = item + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j += 1
        array[item], array[m] = array[m], array[item]
    return array


print("Cортування вибором:")
print(selection(array2))

# Швидке сортування

def quick(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in array:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
    return quick(s_nums) + e_nums + quick(m_nums)
print("Швидке сортування:")
print(quick(array2))
