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

    def get_account_num(self):
        print(Account.count)

    def deposit(self, deposit):
        if deposit < 1:
            print("Error")
        else:
            self.balance += deposit
    
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print("잔액 한도 초과::출금 불가능")
        else:
            self.balance -= withdraw
