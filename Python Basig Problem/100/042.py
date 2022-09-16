import datetime

def sol(a, b):
    day = ["wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue"]
    sel = datetime.date(2022, a, b)
    line = datetime.date(2020, 1, 1)
    i = sel -line
    i = i.days % 7
    print(day[i])


m, d = list(map(int, input().split()))

sol(m, d)

