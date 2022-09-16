s = input()
l = ''
store = s[0]
count = 0

for i in s:
    if i == store:
        count += 1
    else:
        l += store + str(count)
        store = i
        count = 1

l += store + str(count)

print(l)