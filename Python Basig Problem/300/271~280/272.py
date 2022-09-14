import random

class Account:
    count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randrange(0,1000)
        num2 = random.randrange(0,100)
        num3 = random.randrange(0,1000000)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.acc_num = num1 + "-" + num2 + "-" + num3

        Account.count += 1

    def get_account_num():
            print(Account.count)


a = Account("김민수", 100)
b = Account("김철수", 1200)
c = Account("박영희", 4300)
Account.get_account_num()