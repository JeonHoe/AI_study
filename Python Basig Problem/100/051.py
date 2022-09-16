def merge_sort (arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    mid = len_arr // 2
    g1 = merge_sort(arr[:mid])
    g2 = merge_sort(arr[mid:])
    res = []

    while (g1 and g2):
        if (g1[0] < g2 [0]):
            res.append(g1.pop(0))
        else:
            res.append(g2.pop(0))

    while g1:
        res.append(g1.pop(0))
    while g2:
        res.append(g2.pop(0))

    return res

arr1 = [180, 145, 165, 45, 170, 175, 173, 171]

print(merge_sort(arr1))