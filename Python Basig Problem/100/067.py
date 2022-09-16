'''2  1 1
   3  3 2
   4  6 3
   5 10 4
   6 15 5'''

def sol(n):
    sum = 0
    p = 1
    while 1:
        sum += (p-1)
        if n <= sum:
            break
        p += 1
    c =n - (sum - (p - 1))
    return [c, p]

print(sol(59))
    