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
if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            else:
                a, b, c = line.split()
                print(ff(a, b, c))