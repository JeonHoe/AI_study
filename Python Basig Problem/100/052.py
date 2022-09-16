def quick_sort (arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    base = arr.pop(len_arr//2)
    g1 = []
    g2 = []

    for i in range(len_arr - 1):
        if arr[i] < base:
            g1.append(arr[i])
        else:
            g2.append(arr[i])

    return quick_sort(g1) + [base] + quick_sort(g2)


arr = input().split(" ")

print(quick_sort(arr))