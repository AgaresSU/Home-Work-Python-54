# Задача 1: Объединение словарей
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

merged_dict = {**dict1, **dict2, **dict3}
print("Задание 1:")
print(merged_dict)
print("-" * 20)

# Задача 2: Изменение значения в вложенном словаре
employees = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

employees['emp3']['salary'] = 8500

print("Задание 2:")
for emp_id, info in employees.items():
    print(emp_id)
    print(f"name : {info['name']}")
    print(f"salary : {info['salary']}")
print("-" * 20)

# Задача 3: Средний балл студентов
print("Задание 3:")
try:
    num_input = input("Количество студентов: ")
    num_students = int(num_input) if num_input.isdigit() else 0
    students_list = []

    for i in range(1, num_students + 1):
        name = input(f"{i}-й студент: ")
        score = float(input("Балл: "))
        students_list.append({'name': name, 'score': score})

    if num_students > 0:
        avg_score = sum(s['score'] for s in students_list) / num_students
        print(f"\nСредний балл: {avg_score}. Студенты с баллом выше среднего:")
        
        for s in students_list:
            if s['score'] > avg_score:
                print(s['name'])
except EOFError:
    pass
except Exception as e:
    print(f"Произошла ошибка: {e}")
