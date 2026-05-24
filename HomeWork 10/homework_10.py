import math

print("Привет! Это программа для расчета площадей.")

while True:
    print("\n--- Меню ---")
    print("1 - Прямоугольник")
    print("2 - Треугольник")
    print("3 - Круг")
    print("0 - Выход")

    choice = input("Выбери фигуру (введи цифру): ")

    # выход
    if choice == '0':
        print("Пока!")
        break

    try:
        if choice == '1':
            # Прямоугольник
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))

            if a <= 0 or b <= 0:
                print("Ошибка: стороны должны быть больше нуля!")
            else:
                s = a * b
                print("Площадь прямоугольника: {:.2f}".format(s))

        elif choice == '2':
            # Треугольник
            base = float(input("Введите основание: "))
            h = float(input("Введите высоту: "))

            if base <= 0 or h <= 0:
                print("Ошибка: размеры должны быть больше нуля!")
            else:
                s = 0.5 * base * h
                print("Площадь треугольника: {:.2f}".format(s))

        elif choice == '3':
            # Круг
            r = float(input("Введите радиус: "))

            if r <= 0:
                print("Ошибка: радиус должен быть больше нуля!")
            else:
                s = math.pi * (r ** 2)
                print("Площадь круга: {:.2f}".format(s))

        else:
            print("Нет такой цифры в меню!")

    except ValueError:
        print("Ошибка: нужно вводить числа!")
    except Exception:
        print = ("Что-то пошло не так")


# Ссылка на GitHub
# https://github.com/AgaresSU/-10.git