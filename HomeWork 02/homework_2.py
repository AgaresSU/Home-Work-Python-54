# 1
n = int(input("Введите пятизначное число: "))

d1 = n // 10000
d2 = (n // 1000) % 10
d3 = (n // 100) % 10
d4 = (n // 10) % 10
d5 = n % 10

product = d1 * d2 * d3 * d4 * d5
average = (d1 + d2 + d3 + d4 + d5) / 5

print("Произведение цифр:", product)
print("Среднее арифметическое:", average)

# 2


a = float(input("Введите 1-е число: "))
b = float(input("Введите 2-е число: "))
c = float(input("Введите 3-е число: "))
d = float(input("Введите 4-е число: "))

result = (a + b) / (c + d)
print(f"Результат: {result:.2f}")

# 3

x = input("Введите x: ")
y = input("Введите y: ")

print("До обмена:", x, y)
x, y = y, x
print("После обмена:", x, y)
