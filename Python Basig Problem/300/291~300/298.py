num1, num2 = input("숫자 입력:").split()
num1 = int(num1)
num2 = int(num2)

try:
    res = num1 / num2
    print(res)
except ZeroDivisionError:
    print("0으로 나누면 안되요")