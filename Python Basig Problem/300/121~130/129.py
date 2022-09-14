user = input("주민등록번호: ")
div = user[0:-1]; sel = int(user[-1])
div = div.split("-")
div = div[0]+div[1]
arr = list(map(int, div))
cal1 = 0; cnt = 2
for num in arr:
    if cnt > 9:
        cnt = 2
    cal1 += num * cnt
    cnt += 1
cal2 = cal1 % 11
if (11 - cal2) == sel:
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")