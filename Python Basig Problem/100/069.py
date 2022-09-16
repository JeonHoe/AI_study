def sol(num):
    tmp1 = num // 2
    tmp2 = num - tmp1
    while tmp1 > 0:
        if check(tmp1) == 1 and check(tmp2 == 1):
            return [tmp1, tmp2]
        tmp1 -= 1
        tmp2 += 1
    return None, None

def check(num):
    ans = 1
    if num == 1:
        ans = -1
    elif num == 2:
        ans = 1
    else:
        for i in range(2, num):
            if num % i == 0:
                ans = -1
                break
    return ans

print(sol(56))
