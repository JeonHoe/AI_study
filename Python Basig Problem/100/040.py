limit = int(input())
num = int(input())
cnt = 0; kk = 0;
for i in range(num):
    nums = int(input())
    kk += nums
    if kk <= limit:
        cnt += 1
print(cnt)