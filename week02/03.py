import math

def ch(a, b, c):
    if c == "+":
        return a + b
    if c == "-":
        return a - b
    if c == "/":
        if b == 0:
            print("ERROR:Not Division Zero")
            return None
        else:
            return a / b
    if c == "*":
        return a * b

def ff(x):
    x = x.lower()
    if x.find("pi") != -1:
        i = x.index("pi")
        c = x[i+2]
        b = int(x[-1])
        a = math.pi
        x = ch(a, b, c)
    else:
        x = int(x)
    return math.cos(x)

if __name__ == "__main__":
    x = input("입력 : ")
    print(ff(x))
    
