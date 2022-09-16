arr = []

with open("C:/Users/김전호/Desktop/매수종목2.txt", "r") as fp:
    for str in fp.readlines():
        str = str.rstrip("\n")
        arr.append(str)
for i in arr:
    print(i)