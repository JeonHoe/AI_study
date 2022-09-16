def sol(num):
    s = str(num)
    s = s[::-1]
    char = ""
    for i in range(len(s)):
        if i % 3 == 0  and i != 0:
            char += ","
        char += s[i]
    s = char[::-1]
    return s

num = int(input())
print(sol(num))