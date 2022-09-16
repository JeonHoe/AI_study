def solution(data):
    width = len(data[0])
    height = len(data)
    data_sum = [[0] * width for i in range(len(data))]
    for i in range(0, height):
        for j in range(0, width):
            if data[i][j] == 0:
                data_sum[i][j] = 1
            else:
                data_sum[i][j] = 0
    
    for i in range(1, height):
        for j in range(1, width):
            if data_sum[i][j] == 1:
                data_sum[i][j] = min(data_sum[i-1][j-1], min(data_sum[i-1][j], data_sum[i][j-1])) + 1

    maxValue = 0
    x = 0
    y = 0
    for i in range(0, height):
        for j in range(0, width):
            if maxValue < data_sum[i][j]:
                maxValue = data_sum[i][j]
                x = i
                y = j
                
    print(maxValue, 'X', maxValue)
    
    for i in range(x - (maxValue - 1), x + 1):
        for j in range(y - (maxValue - 1), y + 1):
            data[i][j] = '#'

    return data

data = [[0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0]]

re = solution(data)

for line in re:
    for i in line:
        print(i, end="")
    print()