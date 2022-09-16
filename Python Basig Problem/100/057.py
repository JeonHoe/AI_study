def sol(n):
    str1 = ""
    for i in range(n+1):
        str1 += str(i)
    res = 0
    for char in str1:
        if char == "1":
            res+=1
    return res

print(sol(1000))
