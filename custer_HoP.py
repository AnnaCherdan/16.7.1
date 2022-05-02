# О клиенте известна следующая информация: имя, фамилия, город, баланс.
# «Иван Петров. Москва. Баланс: 50 руб.»


class Customer:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'\"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.\"'


cus_1 = Customer('Иван', "Петров", "Москва", 50)
print(cus_1)
print('-' * 20)

# возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты.


class Customer:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}.'

    # def all_customers(self):
    #     return f'{self.name} {self.surname}. {self.city}.'


cus_1 = Customer('Иван', "Петров", "Москва", 50)
cus_2 = Customer('Андрей', "Сидоров", "Кемерово", 70)
cus_3 = Customer('Стас', "Списков", "Владивосток", 80)

all_customers = [cus_1, cus_2, cus_3]
print(cus_1)
print(cus_2)
print(cus_3)

# for guest in all_customers:
#     print(guest.all_customers())
