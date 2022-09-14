user = input("우편번호: ")
sel = user[:3]
if sel in ["010", "011", "012"]:
    print("강북구")
if sel in ["013", "014", "015"]:
    print("도봉구")
if sel in ["016", "017", "018", "019"]:
    print("노원구")
