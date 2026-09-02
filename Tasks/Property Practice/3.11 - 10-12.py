from collections import defaultdict

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.login = login
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    @property
    def balance(self) -> int | float:
        return self.__balance

    @balance.setter
    def balance(self, value: int | float) -> None:
        self.__balance = value

    def deposit(self, value: int | float) -> None:
        self.balance += value

    def is_money_enough(self, value: int | float) -> bool:
        return self.balance >= value

    def payment(self, value: int | float) -> bool | None:
        if not self.is_money_enough(value):
            print('Не хватает средств на балансе. Пополните счет')
            return False

        self.balance -= value
        return True


class Cart:
    def __init__(self, user: User):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, product: Product, quantity: int = 1) -> None:
        self.goods[product] += quantity
        self.__total += product.price * quantity

    def remove(self, product: Product, quantity: int = 1) -> None:
        self.__total = max(self.__total - product.price * self.goods[product], self.__total - product.price * quantity)
        self.goods[product] = max(0, self.goods[product] - quantity)
        if self.goods[product] == 0:
            del self.goods[product]

    @property
    def total(self) -> int | float:
        return self.__total

    def order(self) -> None:
        if not self.user.payment(self.total):
            print('Проблема с оплатой')
            return

        print('Заказ оплачен')

    def print_check(self) -> None:
        print('---Your check---')
        for product, quantity in sorted(self.goods.items(), key=lambda x: x[0].name):
            print(f'{product.name} {product.price} {quantity} {product.price * quantity}')
        print(f'---Total: {self.total}---')

billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20
