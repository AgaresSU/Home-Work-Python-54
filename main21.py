def count_negative_numbers(lst):

    if not lst:
        return 0

    current = 1 if lst[0] < 0 else 0
    return current + count_negative_numbers(lst[1:])


numbers = [-2, 3, 8, -11, -4, 6]
n = count_negative_numbers(numbers)

print(f"Список: {numbers}")
print(f"n = {n}")