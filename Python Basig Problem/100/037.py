str1 = input().split()

dict1 = {}

for i in str1:
    if i in list(dict1.keys()):
        dict1[i] += 1
    else:
        dict1[i] = 1

dict2 = sorted(dict1.items(), key= lambda item: item, reverse=-1)

print(f"{dict2[0][0]}(이)가 총 {dict2[0][1]}표로 반장이 되었습니다.")
