class Human:
    def __init__(self, name, age, s):
        self.name = name
        self.age = age
        self.s = s

    def who(self):
        str1 = ""
        str1 += "이름: " + self.name + ", 나이: " + str(self.age) + ", 성별: " + self.s
        print(str1)

areum = Human(name="조아름", age=25, s="여자")
areum.who()