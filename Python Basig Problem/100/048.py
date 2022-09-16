str1 = input()

res = ""

for i in str1:
    if i.isupper():
        res += i.lower()
    if i.islower():
        res += i.upper()

print(res)
