user = input("현재시간:")
hour, min = user.split(":")
if min == "00":
    print("정각입니다.")
else:
    print("정각이 아닙니다.")
    