
l = [10, 20, 25, 27, 34, 35, 39] #기존 입력 값
n = int(input('순회 횟수는 :'))

def rotate(inL, inN):
    tmp = inL[::]
    arr = []
    for i in range(inN):
        n = inL.pop()
        inL = [n] + inL
    print(tmp)
    print(inL)
    for i, j in zip(tmp, inL):
        print(i, j)
        dif = i - j if i > j else j - i
        arr.append(dif)
    print(arr)
    res = min(arr)
    res = arr.index(res)
    print("index :", res)
    print(f"value : {tmp[res]}, {inL[res]}")    

rotate(l, n)