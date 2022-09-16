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


car = Car(4, 1000)
car.Info()