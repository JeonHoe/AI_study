num = int(input())

if num == 1:
    print("NO")
elif num == 2:
    print("YES")
else:
    for i in range(2,num+1):
        if num%i==0 and i != num:
            print("NO")
            break
        elif i == num:
            print("YES")