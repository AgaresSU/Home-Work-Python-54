class AccountGetSet:
    # Классовые курсы и подписи валют
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    # Приватные свойства счета
    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value

    # Геттер номера счета
    def get_num(self):
        return self.__num

    # Геттер владельца
    def get_surname(self):
        return self.__surname

    # Сеттер владельца
    def set_surname(self, surname):
        self.__surname = surname

    # Геттер процента
    def get_percent(self):
        return self.__percent

    # Сеттер процента
    def set_percent(self, percent):
        self.__percent = percent

    # Геттер баланса
    def get_value(self):
        return self.__value

    # Сеттер баланса
    def set_value(self, value):
        self.__value = value

    # Вывод текущего баланса
    def print_balance(self):
        print(f"Текущий баланс: {self.__value} {AccountGetSet.suffix}")

    # Вывод подробной информации о счете
    def print_info(self):
        print("Информация о счете")
        print("-" * 30)
        print(f"№ счета: {self.__num}")
        print(f"Владелец: {self.__surname}")
        print(f"Проценты: {self.__percent:.0%}")
        self.print_balance()
        print("-" * 30)

    # Статический метод для конвертации
    @staticmethod
    def convert(value, rate):
        return value * rate

    # Конвертация текущего баланса в USD
    def convert_to_usd(self):
        usd_val = AccountGetSet.convert(self.__value, AccountGetSet.rate_usd)
        print(f"Состояние счета: {usd_val} {AccountGetSet.suffix_usd}")

    # Конвертация текущего баланса в EUR
    def convert_to_eur(self):
        eur_val = AccountGetSet.convert(self.__value, AccountGetSet.rate_eur)
        print(f"Состояние счета: {eur_val} {AccountGetSet.suffix_eur}")

    # Изменение курса USD
    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    # Изменение курса EUR
    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    # Изменение владельца счета
    def edit_owner(self, surname):
        self.__surname = surname

    # Начисление процентов на счет
    def add_percents(self):
        self.__value += self.__percent * self.__value
        print("Проценты были успешно начислены.")
        self.print_balance()

    # Снятие денег со счета
    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению, у вас нет {val} {AccountGetSet.suffix}")
        else:
            self.__value -= val
            print(f"{val} {AccountGetSet.suffix} успешно снято.")
        self.print_balance()

    # Пополнение счета
    def add_money(self, val):
        self.__value += val
        print(f"{val} {AccountGetSet.suffix} успешно добавлено.")
        self.print_balance()


class AccountProperty:
    # Классовые курсы и подписи валют
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    # Приватные свойства счета
    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = ""
        self.__percent = 0
        self.__value = 0
        self.surname = surname
        self.percent = percent
        self.value = value

    # Свойство num: только чтение номера счета
    @property
    def num(self):
        return self.__num

    # Свойство surname: чтение владельца
    @property
    def surname(self):
        return self.__surname

    # Свойство surname: изменение владельца
    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    # Свойство percent: чтение процента
    @property
    def percent(self):
        return self.__percent

    # Свойство percent: изменение процента
    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    # Свойство value: чтение баланса
    @property
    def value(self):
        return self.__value

    # Свойство value: изменение баланса
    @value.setter
    def value(self, value):
        self.__value = value

    # Вывод текущего баланса
    def print_balance(self):
        print(f"Текущий баланс: {self.__value} {AccountProperty.suffix}")

    # Вывод подробной информации о счете
    def print_info(self):
        print("Информация о счете")
        print("-" * 30)
        print(f"№ счета: {self.__num}")
        print(f"Владелец: {self.__surname}")
        print(f"Проценты: {self.__percent:.0%}")
        self.print_balance()
        print("-" * 30)

    # Статический метод для конвертации
    @staticmethod
    def convert(value, rate):
        return value * rate

    # Конвертация текущего баланса в USD
    def convert_to_usd(self):
        usd_val = AccountProperty.convert(self.__value, AccountProperty.rate_usd)
        print(f"Состояние счета: {usd_val} {AccountProperty.suffix_usd}")

    # Конвертация текущего баланса в EUR
    def convert_to_eur(self):
        eur_val = AccountProperty.convert(self.__value, AccountProperty.rate_eur)
        print(f"Состояние счета: {eur_val} {AccountProperty.suffix_eur}")

    # Изменение курса USD
    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    # Изменение курса EUR
    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    # Изменение владельца счета
    def edit_owner(self, surname):
        self.surname = surname

    # Начисление процентов на счет
    def add_percents(self):
        self.__value += self.__percent * self.__value
        print("Проценты были успешно начислены.")
        self.print_balance()

    # Снятие денег со счета
    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению, у вас нет {val} {AccountProperty.suffix}")
        else:
            self.__value -= val
            print(f"{val} {AccountProperty.suffix} успешно снято.")
        self.print_balance()

    # Пополнение счета
    def add_money(self, val):
        self.__value += val
        print(f"{val} {AccountProperty.suffix} успешно добавлено.")
        self.print_balance()


# ==========================
# 1) Account: вариант с сеттерами/геттерами
# ==========================
print("AccountGetSet")
acc1 = AccountGetSet("123456", "Долгих", 0.03, 1000)
acc1.print_info()
acc1.convert_to_usd()
acc1.convert_to_eur()
acc1.edit_owner("Дюма")
acc1.print_info()
acc1.add_percents()
acc1.withdraw_money(5000)
acc1.withdraw_money(1000)
acc1.add_money(5000)

print("\n" + "=" * 50 + "\n")

# ==========================
# 2) Account: вариант с @property
# ==========================
print("AccountProperty")
acc2 = AccountProperty("987654", "Иванов", 0.05, 2000)
acc2.print_info()
acc2.convert_to_usd()
acc2.convert_to_eur()
acc2.surname = "Петров"
acc2.print_info()
acc2.add_percents()
acc2.withdraw_money(1000)
acc2.add_money(300)
