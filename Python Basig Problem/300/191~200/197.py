ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in range(1,4):
    if ohlc[i][-1] >= ohlc[i][0]:
        print(ohlc[i][-1])