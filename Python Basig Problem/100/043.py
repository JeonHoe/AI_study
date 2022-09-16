d_num = int(input())
b_num = ""

while d_num != 0:
    b_num += str(d_num % 2)
    d_num = d_num // 2

b_num = b_num[::-1]
print(b_num)