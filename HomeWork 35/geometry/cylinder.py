from .circle import Circle
from .rect import Rectangle


class Cylinder(Rectangle, Circle):
    def __init__(self, r, h):
        Circle.__init__(self, r)
        Rectangle.__init__(self, self.get_circle_circumference(), h)

    def get_volume(self):
        res = self.get_circle_area() * self.h
        print(f"Объем цилиндра {res}")
        return res

    def print_cylinder(self):
        print(f"Радиус основания {self.r}, высота {self.h}")
