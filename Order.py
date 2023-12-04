class Order:
    menu = {
        "Espresso": 6.00,
        "Tea": 5.00,
        "Coffee": 4.50,
        "Milk": 2.50
    }

    def __init__(self, type, customer, barista=''):
        self.type = type
        self.customer = customer
        self.barista = barista
        self.set_price()
        self.set_tip()
        

    def to_string(self):
        return (f'''
{self.customer.name} ordered: {self.type}
Subtotal: ${self.price}
Tips: ${self.tip}
Total: ${self.price + self.tip}
''')
    
    def set_price(self):
        self.price = Order.menu[self.type]

    def set_tip(self):
        self.tip = round(self.customer.tip_rate * self.price, 2)
