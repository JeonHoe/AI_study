fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

user = input("제가 좋아하는 계절은: ")

if user in list(fruit.keys()):
    print("정답입니다.")
else:
    print("오답입니다.")
    