import random

list = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(random.randint(-20, 10))
    list.append(row)

for row in list:
    print(row)


count = 0
for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] < 0:
            count = count + 1

print("Количество отрицательных элементов:", count)

import random

list = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(random.randint(0, 4))
    list.append(row)

for row in list:
    print(row)


product = 1
for i in range(len(list)):
    for j in range(len(list[i])):
        if list[i][j] != 0:
            product = product * list[i][j]

print("Произведение ненулевых элементов:", product)

import random


list = []
for i in range(6):
    row = []
    for j in range(6):
        row.append(random.randint(0, 10))
    list.append(row)


replacement = []
for i in range(6):
    replacement.append(random.randint(0, 10))

print("Одномерный список:", replacement)
print("Исходная матрица:")
for row in list:
    print(row)



for i in range(len(list)):
    if i % 2 != 0:  
        new_row = []
        for j in range(len(replacement)):
            new_row.append(replacement[j])
        list[i] = new_row

print("\nРезультат:")
for row in list:
    print(row)