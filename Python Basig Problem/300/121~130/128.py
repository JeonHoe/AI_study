user = input("주민등록번호: ")
num = user.split("-")[1]
sel = num[1:3]
if sel in ["00", '01', '02', '03', '04', '05', '06', '07', '08']:
    print("서울 입니다.")
else:
    print("서울이 아닙니다.")

