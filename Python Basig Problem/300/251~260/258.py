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


areum = Human("모름", 0, "모름")
areum.setInfo("아름", 25, "여자")
areum.who()