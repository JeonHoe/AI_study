def sol(n):
    k = n % 7
    if k % 3 == 0:
        return n // 7 + k // 3
    else:
        return -1
    
print(sol(int(input())))