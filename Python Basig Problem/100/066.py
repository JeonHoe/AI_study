from re import L


def sol(top, rule):
    sel = []

    for i in range(len(rule)):
        for j in top:
            if j in rule[i]:
                sel.append([j, top.index(j)])
    test = sorted(sel, key=lambda x: x[1])
    if sel == test:
        return "가능"
    else:
        return "불가능"


top = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
rule = "ABD"

res = []
for k in top:
    res.append(sol(k, rule))
print(res)
