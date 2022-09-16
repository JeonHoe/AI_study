def sol(n):
    res = 0
    cnt = 1
    while n > 0:
        if n % 10 in [3, 6, 9]:
            res += ((n % 10) // 3) * cnt
        n = n // 10
        cnt *= 3
    return res

n = int(input())
print(sol(n))