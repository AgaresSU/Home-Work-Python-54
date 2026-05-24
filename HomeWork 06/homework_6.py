# 1)
n = int(input("Введите количество элементов: "))
a = []
i = 0
while i < n:
    x = int(input("Введите число: "))
    a.append(x)
    i += 1
print("Элементы с чётными индексами:")
i = 0
while i < len(a):
    print(a[i], end=" ")
    i += 2
print()

# 2
n = int(input("Введите количество элементов: "))

a = []
i = 0
while i < n:
    x = int(input("Введите число: "))
    a.append(x)
    i += 1
print("Элементы, больше предыдущего:")
i = 1
while i < len(a):
    if a[i] > a[i - 1]:
        print(a[i], end=" ")
    i += 1
print()

#3

n = int(input("Введите высоту треугольника: "))


i = 1
while i <= n:
    c = 1
    while c <= i:
        print("*", end="")
        c += 1
    print()
    i += 1

#3.1
n = int(input("Введите высоту треугольника: "))

i = n
while i >= 1:
    c = 1
    while c <= i:
        print("*", end="")
        c += 1
    print()
    i -= 1

# Дополнительный
size = int(input("Введите размер поля: "))
symbol = int(input("Кол-во символов: "))
i = 0
while i < size:
    c = 0
    while c < symbol:
        n = 0
        while n < size:
            m=0
            while m< symbol:
                if (i + n)%2==0:
                    print("*", end='')
                else:
                    print(" ", end='')
                m+=1
            n += 1
        print()
        c += 1

    i += 1
