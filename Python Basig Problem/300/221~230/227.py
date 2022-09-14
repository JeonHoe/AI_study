def printmxn(string, num):
    cnt = 1
    for i in string:
        if cnt > num:
            print()
            cnt = 1
        print(i, end="")
        cnt += 1

printmxn("아이엠어보이유알어걸", 3)