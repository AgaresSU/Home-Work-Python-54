import os

# --- Задача 1: Обмен местами двух строк в файле ---
print("--- Задача 1: Обмен строк в файле ---")

file_swap = "text_swap.txt"
with open(file_swap, "w", encoding="utf-8") as f:
    f.writelines([
        "Замена строки в текстовом файле;\n",
        "изменить строку в списке;\n",
        "записать список в файл;\n"
    ])

pos1, pos2 = 1, 2
with open(file_swap, "r", encoding="utf-8") as f:
    lines1 = f.readlines()

if pos1 < len(lines1) and pos2 < len(lines1):
    lines1[pos1], lines1[pos2] = lines1[pos2], lines1[pos1]

with open(file_swap, "w", encoding="utf-8") as f:
    f.writelines(lines1)

print("Результат обмена (строки 1 и 2):")
for line in lines1:
    print(line.strip())
print("-" * 30)


# --- Задача 2: Реверсирование строк файла ---
print("--- Задача 2: Реверсирование строк файла ---")

with open(file_swap, "r", encoding="utf-8") as f:
    lines2 = f.readlines()

reversed_lines = lines2[::-1]

with open(file_swap, "w", encoding="utf-8") as f:
    f.writelines(reversed_lines)

print("Результат реверса строк:")
for line in reversed_lines:
    print(line.strip())
print("-" * 30)


# --- Задача 3: Объединение двух файлов ---
print("--- Задача 3: Объединение двух файлов ---")
with open("one.txt", "w", encoding="utf-8") as f:
    f.write("Содержимое первого файла.\n")
with open("two.txt", "w", encoding="utf-8") as f:
    f.write("Содержимое второго файла.\n")


with open("one.txt", "r", encoding="utf-8") as f1:
    data1 = f1.read()
with open("two.txt", "r", encoding="utf-8") as f2:
    data2 = f2.read()

with open("three.txt", "w", encoding="utf-8") as f3:
    f3.write(data1 + data2)

print("Объединение завершено в three.txt.")
with open("three.txt", "r", encoding="utf-8") as f3:
    print("Итог:")
    print(f3.read())