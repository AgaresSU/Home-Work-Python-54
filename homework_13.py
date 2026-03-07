# ДЗ 13
# Задание 1
students_list = [("Иван", 25), ("Мария", 23), ("Петр", 25), ("Анна", 23)]
age_map = {}
for name, age in students_list:
    if age not in age_map:
        age_map[age] = []
    age_map[age].append(name)
print("Задание 1:")
print(age_map)
print("-" * 20)

# Задание 2
nums = [1, 1, 1, 2, 2, 3]
k = 3
threshold = len(nums) // k
counts = {}
for n in nums:
    counts[n] = counts.get(n, 0) + 1
frequent_elements = [num for num, count in counts.items() if count >= threshold]
print("Задание 2:")
print(frequent_elements)
print("-" * 20)

# Задание 3
dict1 = {
    1: {"name": "Иван", "age": 17},
    2: {"name": "Максим", "age": 27},
    3: {"name": "Петр", "age": 30}
}
dict2 = {
    2: {"name": "Мария", "age": 20},
    4: {"name": "Анна", "age": 22}
}
merged_users = {**dict1, **dict2}
result_dict = {uid: info for uid, info in merged_users.items() if info["age"] >= 18}
print("Задание 3:")
print(result_dict)
