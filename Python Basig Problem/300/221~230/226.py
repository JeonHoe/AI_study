def print_5xn(string):
    cnt = 0
    for i in string:
        if cnt > 4:
            print()
            cnt = 0
        print(i, end="")
        cnt += 1


print_5xn("아이엠어보이유알어걸")