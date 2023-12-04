from Person import Person

class Barista(Person):

    def __init__(self, name, favorite_drink, wallet, tip_rate, greeting):
        super().__init__(name, favorite_drink, wallet, tip_rate)
        self.greeting = greeting


