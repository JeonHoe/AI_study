def ff0(num):
    return num * 2

def ff1(num):
    return ff0(num + 2)

def ff2(num):
    num = num + 10
    return ff1(num)

c = ff2(2)
print(c)