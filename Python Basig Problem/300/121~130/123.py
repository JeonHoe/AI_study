exchange_rate = {"달러":1167, "엔":1.096, "유로": 1268, "위안": 171}

num, money = input("입력: ").split()
num = float(num)
if money in list(exchange_rate.keys()):
    res = exchange_rate[money]*num
print(res, "원")
