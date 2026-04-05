import re

# Задание: Найти адрес электронной почты.
print("Задание: Найти адрес электронной почты.")

test_text = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
print("Тест:", test_text)

# [\w.-]+ — ищем буквы (EN/RU), цифры, '_', '.' и '-' до и после собаки
# Используем re.findall, чтобы получить список всех совпадений
emails = re.findall(r"[\w.-]+@[\w.-]+", test_text)

print("\nРезультат:")
print(emails)