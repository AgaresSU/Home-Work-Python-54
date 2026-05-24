from geometry import Circle, Rectangle, Cylinder


circles = [Circle(2), Circle(4), Circle(7), Circle(5), Circle(9), Circle(1), Circle(3), Circle(13), Circle(8)]
rect = [Rectangle(2, 3), Rectangle(4, 8), Rectangle(9, 9), Rectangle(7, 3)]
cylinders = [Cylinder(2, 3), Cylinder(5, 6), Cylinder(7, 8)]

circle_max_s = max(circles, key=lambda c: c.get_circle_area())
rect_min_p = min(rect, key=lambda r: r.get_rect_perimeter())
cylinders_v = list(map(lambda c: c.get_volume(), cylinders))
cylinders_v_avr = sum(cylinders_v) / len(cylinders_v)

print("*" * 20)
print(f"Окружность с наибольшей площадью: {circle_max_s.print_circle()} = {circle_max_s.get_circle_area()}")
print(f"Прямоугольник с наименьшим периметром {rect_min_p.print_rect()} = {rect_min_p.get_rect_perimeter()}")
print(f"Средний объем цилиндров {round(cylinders_v_avr, 2)}")
