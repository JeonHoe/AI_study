dict1 = {}

key = list(input().split())
val = list(map(int, input().split()))

dict1 = dict(zip(key, val))

print(dict1)