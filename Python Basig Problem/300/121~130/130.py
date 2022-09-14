import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

max = float(btc["max_price"])
min = float(btc["min_price"])
change_width = max - min
current = float(btc["opening_price"])

if (current+change_width) > max:
    print("상승장")
else:
    print("하락장")