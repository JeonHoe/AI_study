def print_score(arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum/len(arr))

print_score([1, 2, 3])