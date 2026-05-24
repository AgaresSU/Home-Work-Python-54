from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4

    def draw(self):
        for i in range(self.side):
            print("*" * self.side)

    def print_info(self):
        print("===Квадрат===")
        print("Сторона:", self.side)
        print("Цвет:", self.color)
        print("Площадь:", self.get_area())
        print("Периметр:", self.get_perimeter())
        self.draw()


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def draw(self):
        for i in range(self.length):
            print("*" * self.width)

    def print_info(self):
        print("===Прямоугольник===")
        print("Длина:", self.length)
        print("Ширина:", self.width)
        print("Цвет:", self.color)
        print("Площадь:", self.get_area())
        print("Периметр:", self.get_perimeter())
        self.draw()


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        p = self.get_perimeter() / 2
        return round(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw(self):
        for i in range(1, self.side2):
            print(" " * (self.side2 - i) + "*" * (i * 2 - 1))

    def print_info(self):
        print("===Треугольник===")
        print("Сторона 1:", self.side1)
        print("Сторона 2:", self.side2)
        print("Сторона 3:", self.side3)
        print("Цвет:", self.color)
        print("Площадь:", self.get_area())
        print("Периметр:", self.get_perimeter())
        self.draw()


figures = [
    Square(3, "red"),
    Rectangle(3, 7, "green"),
    Triangle(11, 6, 6, "yellow")
]

for figure in figures:
    figure.print_info()
    print()
