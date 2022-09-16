from email.policy import strict


string = input()
cnt = 0
for i in string:
    if cnt == 2:
        print()
        cnt = 0
    print(i,end="")
    cnt += 1