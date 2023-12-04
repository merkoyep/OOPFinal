from Order import Order
from Person import Person
from Barista import Barista

class CoffeeBar:

    def __init__(self, name, list_of_orders, barista):
        self.name = name
        self.orders_list = list_of_orders
        self.barista = barista
        self.register = 0
        self.receipts = []
        self.tip_jar = 0
    
    def place_order(self, order):
        self.orders_list.append(order)

    def process_orders(self):
        print(self.barista.greeting)
        for order in self.orders_list:
            print(f'{order.customer.name} I have your {order.type} ready!')
            order.customer.wallet -= (order.price + order.tip)
            self.tip_jar += order.tip
            self.register += order.price
            self.receipts.append(order.to_string())
        self.orders_list = []


    def cash_out(self):
        print(f'''
Cashout Summary:
    Today we earned ${self.register}.
    {self.barista.name} took ${self.tip_jar} in tips!


All of Today's Orders:
''')
        for transaction in self.receipts:
            print(transaction)
        self.barista.wallet += self.tip_jar
        self.tip_jar = 0

Kevin = Barista('Kevin', 'Espresso', 10, 0.1, 'Hey dude!')
Marcos_Coffee_Bar = CoffeeBar('Marco\'s Coffee Bar', [], Kevin)

#Challenge 5
Amy = Person('Amy','Coffee', 100, 0.2)
Bob = Person('Bob','Tea', 40, 0.18)
Cat = Person('Mat','Milk', 50, 0.15)
Marcos_Coffee_Bar.place_order(Amy.my_order())
Marcos_Coffee_Bar.place_order(Bob.my_order())
Marcos_Coffee_Bar.place_order(Cat.my_order())
#Challenge 6
Marcos_Coffee_Bar.process_orders()
Marcos_Coffee_Bar.cash_out()