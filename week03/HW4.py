import random


class Dice:
    def __init__(self, value=3, size=1, x=0, y=0):
        self.value = value
        self.size = size
        self.x = x; self.y = y

    def throw(self):
        self.value = random.randrange(1, 7)
        self.x = random.randrange(-100, 100)
        self.y = random.randrange(-100, 100)

    def check(self):
        print(self.value)


if __name__ == "__main__":
    dices = []
    for i in range(6):
        dices.append(Dice(size=random.randrange(1,10)))


    for d in dices:
        d.throw()
        d.check()