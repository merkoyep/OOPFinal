from Order import Order
class Person:

    def __init__(self, name, favorite_drink, wallet, tip_rate):
        self.name = name
        self.favorite_drink = favorite_drink
        self.wallet = wallet
        self.tip_rate = tip_rate

    def my_order(self):
        return Order(self.favorite_drink, self)


#Tests
# marco = Person('marco','latte')
# marcoOrder = marco.my_order()
# print(marcoOrder.to_string())