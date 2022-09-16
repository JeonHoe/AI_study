inputList = []
for i in range(5):
        inputList.extend(input().split())
for i in range(25):
    if inputList[i] == "1":
        inputList[i] = "f"
        if i // 5 != 0:
            inputList[i - 5] = "*"
        if i // 5 != 4:
            inputList[i + 5] = "*"
        if i % 5 != 0:
            inputList[i - 1] = "*"
        if i % 5 != 4:
            inputList[i + 1] = "*"
for i in range(25):
    if i % 5 != 4:
        print(inputList[i], end = "")
    else:
        print(inputList[i], " ")