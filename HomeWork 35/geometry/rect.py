class Rectangle:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get_rect_perimeter(self):
        res = self.l * 2 + self.h * 2
        print(f"Периметр прямоугольника {res}")
        return res

    def get_rect_area(self):
        res = self.l * self.h
        print(f"Площадь прямоугольника {res}")
        return res

    def print_rect(self):
        print(f"Стороны прямоугольника {self.l} {self.h}")
        return self.l, self.h
