import math


class Rectangle:
    # Свойства класса хранятся как private (с двойным подчеркиванием)
    def __init__(self, length, width):
        # Длина прямоугольника (количество строк при рисовании)
        self.__length = length
        # Ширина прямоугольника (количество символов в строке)
        self.__width = width

    # Метод задает новую длину
    def set_length(self, length):
        self.__length = length

    # Метод возвращает длину
    def get_length(self):
        return self.__length

    # Метод задает новую ширину
    def set_width(self, width):
        self.__width = width

    # Метод возвращает ширину
    def get_width(self):
        return self.__width

    # Метод вычисляет площадь прямоугольника
    def get_area(self):
        return self.__length * self.__width

    # Метод вычисляет периметр прямоугольника
    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

    # Метод вычисляет диагональ (в задании названо "гипотенуза")
    def get_diagonal(self):
        return math.sqrt(self.__length ** 2 + self.__width ** 2)

    # Метод рисует прямоугольник символом "*"
    def draw(self):
        for i in range(self.__length):
            print("*" * self.__width)


class KgToPounds:
    # В private-свойстве хранится количество килограммов
    def __init__(self, kg):
        self.__kg = 0
        self.kg = kg

    # Геттер для чтения килограммов через свойство kg
    @property
    def kg(self):
        return self.__kg

    # Сеттер для записи килограммов через свойство kg
    # Здесь выполняется проверка, что значение является числом
    @kg.setter
    def kg(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__kg = value
        else:
            print("Килограммы задаются только числами")

    # Метод переводит килограммы в фунты
    def to_pounds(self):
        return self.__kg * 2.205


# ==========================
# Задание 1: Rectangle
# ==========================
r1 = Rectangle(3, 9)
print("Длина прямоугольника:", r1.get_length())
print("Ширина прямоугольника:", r1.get_width())
print("Площадь прямоугольника:", r1.get_area())
print("Периметр прямоугольника:", r1.get_perimeter())
print("Гипотенуза прямоугольника:", round(r1.get_diagonal(), 2))
r1.draw()

print()

# ==========================
# Задание 2: KgToPounds
# ==========================
k1 = KgToPounds(12)
print(f"{k1.kg} кг => {k1.to_pounds()} фунтов")

k2 = KgToPounds(41)
print(f"{k2.kg} кг => {k2.to_pounds()} фунтов")

# Проверка: если попытаться передать не число, будет сообщение об ошибке
k2.kg = "сорок"
