class Car:
    def __init__(self, wheal, price):
        self.wheal = wheal
        self.price = price

class Bike(Car):
    pass

car = Car(2, 1000)
print(car.wheal)
print(car.price)