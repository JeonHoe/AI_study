tel = {"011": "SKT", "016": "KT", "019":"LGU", "010": "unknown"}

user = input("휴대전화 번호 입력: ")
sel, *ver = user.split("-")
if sel == "011":
    print("당신은 %s 사용자입니다." % tel[sel])
elif sel == "016":
    print("당신은 %s 사용자입니다." % tel[sel])
elif sel == "019":
    print("당신은 %s 사용자입니다." % tel[sel])
elif sel == "010":
    print("당신의 통신사를 알 수 없습니다.")