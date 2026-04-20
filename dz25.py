class Book:
    # Конструктор: при создании объекта задаем значения по умолчанию
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    # Метод для ввода данных о книге с клавиатуры
    def input_data(self):
        self.title = input("Введите название книги: ")

        # Год выпуска должен быть целым числом
        while True:
            try:
                self.year = int(input("Введите год выпуска: "))
                break
            except ValueError:
                print("Ошибка: год должен быть целым числом.")

        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")

        # Цена может быть целой или вещественной
        while True:
            try:
                self.price = float(input("Введите цену: "))
                break
            except ValueError:
                print("Ошибка: цена должна быть числом.")

    # Метод для вывода всех данных о книге
    def print_data(self):
        print("\n" + "=" * 40)
        print("Информация о книге")
        print("-" * 40)
        print("Название:", self.title)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)
        print("=" * 40)

    # Ниже методы доступа к отдельным полям (set/get)
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


# Создаем объект книги
book1 = Book()

# Заполняем поля через метод класса
book1.input_data()

# Выводим данные книги
book1.print_data()

# Пример доступа к отдельному полю через методы класса
print("\nДоступ к отдельным полям через методы:")
print("Название книги:", book1.get_title())
print("Цена книги:", book1.get_price())

# Пример изменения поля через метод set_...
book1.set_price(999.99)
print("Новая цена книги после изменения:", book1.get_price())
