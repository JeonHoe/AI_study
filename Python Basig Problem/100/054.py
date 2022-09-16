def sol(str):
    arr = list(map(int,str.split(" ")))
    arr.sort()

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff > 1:
            print("NO")
            break
        if i == len(arr) - 1:
            print("YES")
    


string = input()
sol(string)