import numpy as np

square = 5
dictact = 3

round = [[1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0]]

round =np.array(round)

s = 0
for i in range(square - dictact + 1):
    for j in range(dictact):
        if np.sum(round[i:dictact+i, j:dictact+j]) > s: 
            s = np.sum(round[i:dictact+i, j:dictact+j])
print(s)