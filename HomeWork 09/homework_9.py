def convert_temperature(value, scale):
    if scale == "C":
        result = value * 9 / 5 + 32
        return str(value) + "C = " + str(round(result, 2)) + "F"
    elif scale == "F":
        result = (value - 32) * 5 / 9
        return str(value) + "F = " + str(round(result, 2)) + "C"
    else:
        return "Ошибка: используйте 'C' или 'F'"

print(convert_temperature(32, "C"))
print(convert_temperature(318, "F"))

def change(lst):
    first = lst[0]
    lst[0] = lst[len(lst) - 1]
    lst[len(lst) - 1] = first
    return lst

print(change([1, 2, 3]))
print(change([9, 12, 33, 54, 105]))
print(change(["С", "Л", "О", "Н"]))