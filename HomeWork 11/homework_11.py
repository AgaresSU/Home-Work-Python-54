#1
print("Задание 1: Поиск заданного элемента в кортеже")
my_tuple = ('ab', 'abcd', 'cde', 'abc', 'def')
print(f"Исходный кортеж: {my_tuple}")
print()

s = input("s = ")

if s in my_tuple:
    print("Yes")
else:
    print("No")

print()
print("=" * 40)
print()

#2
print("Задание 2: Статистика частотности символов в кортеже")
print()

user_input = input("Введите по порядку, без пробелов, элементы кортежа: ")

tuple_elements = tuple(user_input)
print(tuple_elements)

unique_elements = set(tuple_elements)

for element in sorted(unique_elements):
    count = tuple_elements.count(element)
    print(f"Количество {element} = {count}")

print()
print("=" * 40)
print()

#3
print("Задание 3: Лотерея")
print()

winning_numbers = {7, 15, 23, 42, 56}

while True:
    try:
        user_number = int(input("Введите ваше число (или 0 для выхода): "))

        if user_number == 0:
            print("Игра завершена. До свидания!")
            break

        if user_number in winning_numbers:
            print("Поздравляем, вы угадали!")
        else:
            print("Попробуйте еще раз.")

    except ValueError:
        print("Ошибка: нужно ввести целое число!")
