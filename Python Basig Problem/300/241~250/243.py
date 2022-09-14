import datetime

now = datetime.datetime.now()

for i in range(5,0,-1):
    days = datetime.timedelta(i)
    print(now-days)
