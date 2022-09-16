def sol(n, k):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    start = 0
    while True:
        size = len(arr)
        if size == 2:
            return arr
        arr.pop(0)
        arr = arr[2:] + arr[:2]
    
    
n, k = [int(i) for i in input().split()]
print(sol(n,k))

"""1 2 3 4 5 6, 2 3 4 5 6, 4 5 6 2 3, 5 6 2 3, 2 3 5 6"""
