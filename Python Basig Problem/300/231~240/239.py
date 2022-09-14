def ff1(num):
    return num + 4

def ff2(num):
    num = num + 2
    return ff1(num)

c = ff2(10)
print(c)