num = int(input())

for i in range(num):
    for j in range(i+5):
        if j < 4-i:
            print(" ",end="")
        else:
            print("*",end="")
    print()