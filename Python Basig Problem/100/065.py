a = input().split()
b = input().split()
c = []

arr = list(zip(a, b))

for i in range(len(arr)):
    if i % 2 == 0:
        c.append(list(arr[i]))
    else:
        c.append(list(arr[i][::-1]))


print(c)
    