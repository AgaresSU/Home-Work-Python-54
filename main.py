# Задание 1
mult = lambda x, y, z: x * y * z
print(mult(2, 5, 5))
print()

# Задание 2
students_2 = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

# Сортировка по имени (по алфавиту / возрастанию)
sorted_by_name = sorted(students_2, key=lambda item: item['name'])
print(sorted_by_name)

# Сортировка по оценкам (в порядке убывания)
sorted_by_final_desc = sorted(students_2, key=lambda item: item['final'], reverse=True)
print(sorted_by_final_desc)
print()

# Задание 3
students_3 = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

max_student = max(students_3, key=lambda item: item['final'])
print(max_student)

min_student = min(students_3, key=lambda item: item['final'])
print(min_student)
print()

# Задание 4
nums = [3, 5, 7, 3, 9, 5, 7, 2]

# Возведение в квадрат
squares = list(map(lambda x: x ** 2, nums))
print(squares)

# Возведение в куб
cubes = list(map(lambda x: x ** 3, nums))
print(cubes)
