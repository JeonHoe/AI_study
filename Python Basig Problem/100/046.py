str1 = ""
for i in range(1,101):
    str1+=str(i)
res = 0
for j in str1:
    res += int(j)
print(res)