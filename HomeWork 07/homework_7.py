
a = [3, 7, 2, 5, 2, 8, 3, 9, 5, 1, 7, 4, 3, 6, 1]
print("Исходнный список:", a)

delete = [8, 9, 4, 6]
print("Удалить значения:", delete)

new = []
i = 0
while i < len(a):
    if a[i] not in delete:
        new.append(a[i])
    i += 1

print("После удаления:", new)

n = len(new)
i = 0
while i < n - 1:
    a = 0
    while a < n - 1 - i:
        if new[a] > new[a + 1]:
            temp = new[a]
            new[a] = new[a + 1]
            new[a + 1] = temp
        a += 1
    i += 1

print("Отсортированный список:", new)