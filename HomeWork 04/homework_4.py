print("Калькулятор Готов!")

while True:
    #меню
    print("\nВыберите операцию:")
    print("1 - \"r\"  - применяет унарный минус к операнду")
    print("2 - \"+\"  - сложение")
    print("3 - \"-\"  - вычитание")
    print("4 - \"/\"  - деление")
    print("5 - \"*\"  - умножение")
    print("6 - \"%%\" - деление по модулю (остаток от деления)")
    print("7 - \"<\"  - минимальное из двух чисел")
    print("8 - \">\"  - максимальное из двух чисел")
    print("0 - \"STOP\" - остановить работу")

    # Шаг 2: Ввод номера операции
    try:
        choice = input("Введите номер операции: ")
        if choice == "0":
            print("Работа завершена. До свидания!")
            break
    except Exception as e:
        print("Ошибка при вводе номера операции.")

    if not choice.isdigit():
        print("Ошибка: введите число (0–8).")
        continue

    op_num = int(choice)

    if op_num < 1 or op_num > 8:
        print("Неверный номер операции. Должно быть от 1 до 8.")
        continue


    try:
        a = float(input("Введите первое число: "))
    except ValueError:
        print("Ошибка: введите число (целое или дробное).")
        continue  # Возвращаемся

    if op_num == 1:  # унарный -
        result = -a
        print(f"Унарный минус: -({a}) = {result}")
        continue  

    try:
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введите число (целое или дробное).")
        continue

    if op_num == 2:
        result = a + b
        print(f"{a} + {b} = {result}")

    elif op_num == 3:
        result = a - b
        print(f"{a} - {b} = {result}")

    elif op_num == 4:
        if b == 0:
            print("Ошибка: деление на ноль невозможно!")
            continue
        result = a / b
        print(f"{a} / {b} = {result}")

    elif op_num == 5:
        result = a * b
        print(f"{a} * {b} = {result}")

    elif op_num == 6:
        if b == 0:
            print("Ошибка: деление по модулю на ноль невозможно!")
            continue
        result = a % b
        print(f"{a} % {b} = {result}")

    elif op_num == 7: 
        if a <= b:
            result = a
        else:
            result = b
        print(f"Минимум из {a} и {b} = {result}")

    elif op_num == 8:
        if a >= b:
            result = a
        else:
            result = b
        print(f"Максимум из {a} и {b} = {result}")