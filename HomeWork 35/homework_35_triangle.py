class Integer:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Сторона должна быть положительным целым числом")
        setattr(instance, self.name, value)


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.")
        else:
            print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.")


tr1 = Triangle(2, 5, 6)
tr2 = Triangle(5, 2, 8)
tr3 = Triangle(7, 3, 6)

tr1.check_triangle()
tr2.check_triangle()
tr3.check_triangle()
