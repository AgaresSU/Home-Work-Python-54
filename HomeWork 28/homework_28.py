class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def is_digit(self):
        if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
            print("Координаты должны быть числом")
            return False
        return True

    def is_int(self):
        if not isinstance(self.__x, int) or not isinstance(self.__y, int):
            print("Координаты должны быть целочисленными")
            return False
        if self.__x < 0 or self.__y < 0:
            print("Координаты должны быть положительными")
            return False
        return True


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "green", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def set_coords(self, sp, ep):
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep


class Line(Prop):
    def draw_line(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def set_coords(self, sp, ep):
        if sp.is_int() and ep.is_int():
            self._sp = sp
            self._ep = ep


class Rect(Prop):
    def draw_rect(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


line = Line(Point(1, 2), Point(10, 20), "red", 1)
line.draw_line()

line.set_coords(Point(10.2, 20), Point(100, 200))
line.draw_line()

line.set_coords(Point(-2, 20), Point(100, 200))
line.draw_line()

rect = Rect(Point(7, 9), Point(12, 15), "red", 1)
rect.draw_rect()

rect.set_coords(Point(30.5, 40.2), Point(50, 60))
rect.draw_rect()
