import pickle


def save_data(filename, countries):
    with open(filename, "wb") as f:
        pickle.dump(countries, f)
    print("Файл сохранен")


def load_data(filename):
    try:
        with open(filename, "rb") as f:
            countries = pickle.load(f)
    except FileNotFoundError:
        countries = {}
    return countries


def add_data(countries):
    country = input("Введите название страны (с заглавной буквы): ")
    capital = input("Введите название столицы страны (с заглавной буквы): ")
    countries[country] = capital


def delete_data(countries):
    country = input("Введите название страны: ")
    if country in countries:
        del countries[country]
    else:
        print("Такой страны нет")


def search_data(countries):
    country = input("Введите название страны: ")
    if country in countries:
        print(country, "-", countries[country])
    else:
        print("Такой страны нет")


def edit_data(countries):
    country = input("Введите название страны: ")
    if country in countries:
        capital = input("Введите новое название столицы: ")
        countries[country] = capital
    else:
        print("Такой страны нет")


def show_data(countries):
    print(countries)


filename = "countries.txt"
countries = load_data(filename)

while True:
    print("*" * 30)
    print("Выбор действия:")
    print("1 - добавление данных")
    print("2 - удаление данных")
    print("3 - поиск данных")
    print("4 - редактирование данных")
    print("5 - просмотр данных")
    print("6 - завершение работы")
    action = input("Ввод: ")

    if action == "1":
        add_data(countries)
        save_data(filename, countries)
    elif action == "2":
        delete_data(countries)
        save_data(filename, countries)
    elif action == "3":
        search_data(countries)
    elif action == "4":
        edit_data(countries)
        save_data(filename, countries)
    elif action == "5":
        show_data(countries)
    elif action == "6":
        break
    else:
        print("Неверный ввод")
