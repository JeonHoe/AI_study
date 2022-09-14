ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

res = 0

for i in range(1,4):
    res += (ohlc[i][-1]- ohlc[i][0])

print(res)