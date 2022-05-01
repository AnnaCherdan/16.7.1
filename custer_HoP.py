# О клиенте известна следующая информация: имя, фамилия, город, баланс.
# «Иван Петров. Москва. Баланс: 50 руб.»


class Customer:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'


cus_1 = Customer('Иван', "Петров", "Москва", 50)
print(cus_1)