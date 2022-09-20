import math

def ff(x):
    return 1 / (1 + math.exp(-x))

def gg(x):
    return ff(x)*(1-ff(x))


if __name__ == "__main__":
    n = int(input())
    print(gg(n))
