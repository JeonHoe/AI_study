import random

class Account:
    acc_count = 0
    def __init__(self, name, balance):
        self.name = name
        if type(balance) is str:
            balance = balance.replace(",", "")
            balance = int(balance)
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randrange(0,1000)
        num2 = random.randrange(0,100)
        num3 = random.randrange(0,1000000)
        
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.acc_num = num1 + "-" + num2 + "-" + num3
        self.deposit_count = 0

        Account.acc_count += 1

    def get_account_num(self):
        print(Account.acc_count)

    def deposit(self, deposit):
        if deposit < 1:
            print("Error")
        else:
            self.balance += deposit
            self.deposit_count += 1
            if self.deposit_count == 5:
                self.balance *= 1.01
                self.deposit_count = 0
    
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print("잔액 한도 초과::출금 불가능")
        else:
            self.balance -= withdraw

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주 :", self.name)
        print("계좌번호:", self.acc_num)
        str_balance = str(self.balance)
        str_balance = str_balance[::-1]
        char = ""
        for i in range(len(str_balance)):
            if i % 3 == 0  and i != 0:
                char += ","
            char += str_balance[i]
        str_balance = char[::-1]
        print("잔고:", str_balance)



a = Account("파이썬", "1,100,000")
a.display_info()
