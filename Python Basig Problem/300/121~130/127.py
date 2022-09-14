user = input("주민등록번호: ")
sel = user.split("-")[1]
if sel[0] in ["1", "3"]:
    print("남자")
if sel[0] in ["2", "4"]:
    print("여자")
