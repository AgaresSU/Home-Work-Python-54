# Часть 1. Пример Prop -> Line/Rect
class Point:
    # Класс точки с координатами x и y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Переопределяем вывод объекта, чтобы точка печаталась красиво
    def __str__(self):
        return f"({self.x}, {self.y})"


class Prop:
    # Базовый класс графического примитива
    def __init__(self, sp: Point, ep: Point, color: str = "green", width: int = 1):
        self._sp = sp           # protected: начальная точка
        self._ep = ep           # protected: конечная точка
        self._color = color     # protected: цвет
        self.__width = width    # private: толщина

    # Геттер private-свойства ширины
    def get_width(self):
        return self.__width


class Line(Prop):
    # Класс линии, наследуется от Prop
    def __init__(self, *args):
        super().__init__(*args)
        self.__width = 5  # private-свойство именно этого класса (для примера)

    # Вывод параметров линии
    def draw_line(self):
        print(
            f"Рисование линии: {self._sp}, {self._ep}, {self._color}, "
            f"{self.__width}, {self.get_width()}"
        )


class Rect(Prop):
    # Класс прямоугольника, наследуется от Prop
    def __init__(self, sp, ep, color="green", width=1, bg="yellow"):
        super().__init__(sp, ep, color, width)
        self.background = bg  # цвет фона

    # Вывод параметров прямоугольника
    def draw_rect(self):
        print(
            f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, "
            f"{self.get_width()}, {self.background}"
        )


line = Line(Point(1, 2), Point(10, 20), "red", 2)
line.draw_line()

rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()

print(line.__dict__)

print("-" * 50)



# Часть 2. Пример Figure -> Rectangle
class Figure:
    # Базовый класс фигуры, хранит цвет
    def __init__(self, color):
        self.__color = color

    # Геттер цвета
    @property
    def color(self):
        return self.__color

    # Сеттер цвета
    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    # Класс прямоугольника, наследуется от Figure
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    # Геттер ширины
    @property
    def width(self):
        return self.__width

    # Сеттер ширины с проверкой
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("Ширина должна быть больше 0")

    # Геттер высоты
    @property
    def height(self):
        return self.__height

    # Сеттер высоты с проверкой
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError("Высота должна быть больше 0")

    # Метод вычисления площади
    def area(self):
        print(f"Площадь {self.color} прямоугольника:")
        return self.width * self.height


r = Rectangle(10, 20, "green")
r.width = 5
print("Ширина:", r.width)
print("Высота:", r.height)
print("Цвет:", r.color)
r.color = "Красный"
print("Новый цвет:", r.color)
print("Площадь:", r.area())
