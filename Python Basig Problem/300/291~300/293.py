import csv

with open("C:/Users/김전호/Desktop/매수종목.csv", "wt", encoding="cp949", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", "15.79"])
    writer.writerow(["NAVER", "035420", "55.82"])