# 1. Удаление фрагмента между 'h'
print("Задание 1:")
s1 = input("Введите строку: ")
first_h = s1.find('h')
last_h = s1.rfind('h')

if first_h != -1 and last_h != -1:
    res1 = s1[:first_h] + s1[last_h + 1:]
    print(res1)
else:
    print("Буква 'h' не найдена дважды.")
print("-" * 20)

# 2. Разворот фрагмента между 'h'
print("Задание 2:")
s2 = input("Введите строку: ")
first_h2 = s2.find('h')
last_h2 = s2.rfind('h')

if first_h2 != -1 and last_h2 != -1:
    # Берем часть строго между первым и последним 'h'
    middle = s2[first_h2 + 1:last_h2]
    # Собираем: до первого 'h' + сам 'h' + развернутая середина + последний 'h' + остаток
    res2 = s2[:first_h2 + 1] + middle[::-1] + s2[last_h2:]
    print(res2)
else:
    print("Буква 'h' не найдена дважды.")
print("-" * 20)

# 3. Замена подстроки
print("Задание 3:")
s3 = input("Строка: ")
old_sub = input("Ее заменяемая подстрока: ")
new_sub = input("Новая подстрока: ")
print(s3.replace(old_sub, new_sub))
print("-" * 20)

# 4. Подсчет слов на букву 'е'
print("Задание 4:")
text = """
Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели.
"""
print("Тестовый текст:", text.strip())

words = text.split()
count = 0
for word in words:
    # Проверяем первую букву (в нижнем регистре для учета 'Е' и 'е')
    # Используем .startswith() или просто обращение по индексу [0]
    if word.lower().startswith('е'):
        count += 1

print("Количество слов:", count)