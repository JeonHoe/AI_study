user = int(input("입력값: "))
res = user + 20
if res > 255:
    res = 255
print("출력값: %d" % res)