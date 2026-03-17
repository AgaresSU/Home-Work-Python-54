import math


def calculate_area(figure_type, **kwargs):
    if figure_type == 'rhombus':
        d1 = kwargs.get('d1')
        d2 = kwargs.get('d2')
        return (d1 * d2) / 2

    elif figure_type == 'square':
        a = kwargs.get('a')
        return a ** 2

    elif figure_type == 'trapezoid':
        a = kwargs.get('a')
        b = kwargs.get('b')
        h = kwargs.get('h')
        return 0.5 * (a + b) * h

    elif figure_type == 'circle':
        r = kwargs.get('r')
        return math.pi * (r ** 2)

    else:
        return "invalid data"


print(calculate_area(figure_type='rhombus', d1=10, d2=8))
print(calculate_area(figure_type='square', a=5))
print(calculate_area(figure_type='trapezoid', a=12, b=3, h=6))
print(calculate_area(figure_type='circle', r=18))
print(calculate_area(figure_type='unknown', a=1, b=2, c=3))
