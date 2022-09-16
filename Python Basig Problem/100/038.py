score = list(map(int, input().split()))


dict1 = {}

for i in score:
    if i in list(dict1.keys()):
        dict1[i] += 1
    else:
        dict1[i] = 1

dict2 = sorted(dict1.items(), key= lambda item: item, reverse=-1)
print(dict2[0][1]+dict2[1][1]+dict2[2][1])