import os


def create_tree(base_dir):
    # Создаем корневую папку Work, если ее еще нет
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    # Создаем папки первого уровня
    f1_dir = os.path.join(base_dir, "F1")
    f2_dir = os.path.join(base_dir, "F2")
    if not os.path.exists(f1_dir):
        os.mkdir(f1_dir)
    if not os.path.exists(f2_dir):
        os.mkdir(f2_dir)

    # Создаем вложенную папку F21 внутри F2
    f21_dir = os.path.join(f2_dir, "F21")
    if not os.path.exists(f21_dir):
        os.mkdir(f21_dir)

    # Создаем и заполняем файлы (часть файлов по условию с текстом, остальные пустые)
    files_data = {
        os.path.join(base_dir, "w.txt"): "Это файл w.txt\n",
        os.path.join(f1_dir, "f11.txt"): "",
        os.path.join(f1_dir, "f12.txt"): "Это файл f12.txt\n",
        os.path.join(f1_dir, "f13.txt"): "",
        os.path.join(f21_dir, "f211.txt"): "Это файл f211.txt\n",
        os.path.join(f21_dir, "f212.txt"): "Это файл f212.txt\n",
    }

    for file_path in files_data:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(files_data[file_path])


def print_walk_bottom_up(base_dir):
    # Обход дерева снизу вверх (сначала дочерние папки, потом родительские)
    print("Обход Work снизу вверх")
    for root, dirs, files in os.walk(base_dir, topdown=False):
        print(root)
        print(dirs)
        print(files)


def print_walk_top_down(base_dir):
    # Обход дерева сверху вниз (сначала родительская папка, потом дочерние)
    print("Обход Work сверху вниз")
    for root, dirs, files in os.walk(base_dir):
        print(root)
        print(dirs)
        print(files)


def main():
    base_dir = "Work"
    create_tree(base_dir)
    print_walk_bottom_up(base_dir)
    print("-" * 60)
    print_walk_top_down(base_dir)


main()
