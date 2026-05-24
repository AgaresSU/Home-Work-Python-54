class Order:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.name == "_price" or self.name == "_quantity":
            if value <= 0:
                raise ValueError("Значение должно быть положительным")
        setattr(instance, self.name, value)


class Product:
    name = Order()
    price = Order()
    quantity = Order()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_sum(self):
        return self.price * self.quantity


order = Product("apple", 5, 10)
print(order.total_sum())
