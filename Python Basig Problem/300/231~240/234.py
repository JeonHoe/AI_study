def pickup_even(arr):
    res = []
    for i in arr:
        if i%2==0:
            res.append(i)
    print(res)

pickup_even([3,4,5,6,7,8])