from time import ctime


tbs = ["12:30", "13:20", "14:13"]
ct = "12:40"

def sol(tbs, ct):
    arr = []; res = []
    ct = ct.strip('"')
    ct = ctime(ct)
    for i in tbs:
        i = i.strip('"')
        i = ctime(i)
        arr.append(i - ct)
    for k in arr:
        if k < 0:
            res.append("지나갔습니다")
        else:
            h = k // 60
            m = k % 60
            h = str(h)
            m = str(m).zfill(2)
            s = h + "시간 " + m + "분"
            res.append(s)
    return res
            

def ctime(ct):
    if type(ct) is str:
        arr = list(map(int,ct.split(":")))
    res = 60 * arr[0] + arr[1]
    return res

    

print(sol(tbs, ct))