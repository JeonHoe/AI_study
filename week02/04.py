def ff(a, b, c):
    a = int(a);  b = int(b)
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
    else:
        print("ERROR")
        return None




a ,b, c = input("입력 : ").split()

print("출력 :", ff(a, b, c))