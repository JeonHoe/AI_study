class Human:
    def __init__(self, name, age, s):
        self.name = name
        self.age = age
        self.s = s

    def who(self):
        str1 = ""
        str1 += "이름: " + self.name + ", 나이: " + str(self.age) + ", 성별: " + self.s
        print(str1)

    def setInfo(self, name, age, s):
        self.name = name
        self.age = age
        self.s = s

    def __del__(self):
        print("나의 죽음을 알리지 마라")
    


areum = Human("모름", 0, "모름")
del areum