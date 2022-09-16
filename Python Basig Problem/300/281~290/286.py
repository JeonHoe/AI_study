class Car:
    def __init__(self, wheal, price):
        self.wheal = wheal
        self.price = price

    def Info(self):
        print("바퀴 수:", self.wheal)
        print("가격 :", self.price)

class Bike(Car):
    def __init__(self, wheal, price, act):
        Car.__init__(self, wheal, price)
        self.act = act

    def Info(self):
        Car.Info(self)


bicycle = Bike(2, 100, "시마노")
bicycle.Info()