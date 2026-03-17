# Задание 1: Декоратор repeat(n)

def repeat(n):
    def my_decorator(func):
        def wrap(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrap
    return my_decorator

@repeat(3)
def say_hi():
    print("Hi")

say_hi()
print()


# Задание 2: Декоратор, умножающий результат на 2

def multiply_by_2(func):
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        return res * 2
    return wrap

@multiply_by_2
def summa(a, b):
    return a + b

print(summa(a=2, b=3))
print()

# Задание 3: Декоратор, проверяющий is_admin
is_admin = False

def check_admin(func):
    def wrap(*args, **kwargs):
        if is_admin:
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен!")
    return wrap

@check_admin
def say_hello_world():
    print("Hello World")

say_hello_world()

is_admin = True
say_hello_world()
print()

# Задание 4: Декоратор "Начало" и "Конец"
def start_end_decorator(func):
    def wrap(*args, **kwargs):
        print("Начало")
        func(*args, **kwargs)
        print("Конец")
    return wrap

@start_end_decorator
def print_greetings():
    print("Привет!")

print_greetings()
