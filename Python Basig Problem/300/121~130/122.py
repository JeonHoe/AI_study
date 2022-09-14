score = int(input("score: "))
if 80 < score < 100:
    grade = "A"
elif 60 < score:
    grage = "B"
elif 40 < score:
    grade = "C"
elif 20 < score:
    grade = "D"
else:
    grade = "E"
print("grade is", grade)