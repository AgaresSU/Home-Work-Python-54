import os
from datetime import datetime


def format_size(size_in_bytes):
    """Преобразует размер из байт в удобный вид."""
    if size_in_bytes < 1024:
        return str(size_in_bytes) + " Б"
    if size_in_bytes < 1024 * 1024:
        return f"{size_in_bytes / 1024:.2f} КБ"
    return f"{size_in_bytes / (1024 * 1024):.2f} МБ"


# Шаг 1-2: запрашиваем путь у пользователя
path = input("Введите путь к файлу или папке: ").strip()

# Если пользователь ничего не ввел - выходим
if path == "":
    print("Путь не введен.")
else:
    # Шаг 3: проверяем, существует ли путь
    if not os.path.exists(path):
        print("Указанный путь не существует.")
    else:
        # Шаг 4: получаем абсолютный путь
        abs_path = os.path.abspath(path)

        # Шаг 5: определяем тип объекта (файл / директория)
        if os.path.isfile(path):
            obj_type = "Файл"
        elif os.path.isdir(path):
            obj_type = "Директория"
        else:
            obj_type = "Неизвестный тип"

        # Выводим общий блок информации
        print("=" * 45)
        print("Информация о пути")
        print("-" * 45)
        print("Исходный путь:", path)
        print("Абсолютный путь:", abs_path)
        print("Тип объекта:", obj_type)

        # Шаг 6: если это файл, показываем размер и дату изменения
        if os.path.isfile(path):
            file_size = os.path.getsize(path)
            changed_ts = os.path.getmtime(path)

            # Преобразуем timestamp в читаемую дату/время
            changed_time = datetime.fromtimestamp(changed_ts).strftime("%d.%m.%Y %H:%M:%S")

            print("Размер:", file_size, "байт")
            print("Размер (удобный вид):", format_size(file_size))
            print("Последнее изменение:", changed_time)

        print("=" * 45)
