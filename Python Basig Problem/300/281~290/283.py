class Car:
    def __init__(self, wheal, price):
        self.wheal = wheal
        self.price = price

class Bike(Car):
    pass

bicycle = Bike(2, 100)
print(bicycle.price)