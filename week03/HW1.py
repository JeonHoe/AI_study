if __name__ == "__main__":
    summary = 0
    days = 0
    with open("sales.txt", "r") as inFp:
        while True:
            line = inFp.readline()
            if not line:
                break
            line = int(line)
            summary += line
            days += 1

    avrg_days = summary / days

    print(summary)
    print(days)
    print(avrg_days)

    with open("summary.txt", "w", encoding="UTF-8") as outFp:
        str1 = "총매출 = " + str(summary) + "\n"
        str2 = "평균 일매출 = " + str(avrg_days)
        outFp.write(str1)
        outFp.write(str2)
