data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
res = []
for i in range(3):
    for j in range(4):
        res.append(data[i][j]*1.00014)

print(res)