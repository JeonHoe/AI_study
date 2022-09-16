class Car:
    def __init__(self, wheal, price):
        self.wheal = wheal
        self.price = price

class Bike(Car):
    def __init__(self, wheal, price, act):
        Car.__init__(self, wheal, price)
        self.act = act

        


bicycle = Bike(2, 100, "시마노")
print(bicycle.act)