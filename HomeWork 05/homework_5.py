num = 25

print("Я загадал число от 1 до 100.")
print("Попробуй угадать!")
print("Устал - введи 0.")

attempt = 0

while True:
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Неправильный ввод! Нужно целое число.")
        continue
    if number == 0:
        print("Вы вышли из игры.")
        break

    attempt = attempt + 1

    if number == num:
        print("Вы угадали загаданное число с", attempt, "раза")
        break
    elif number < num:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")