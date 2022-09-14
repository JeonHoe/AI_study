def print_keys (dict1):
    if type(dict1) == dict:
        for i in list(dict1.keys()):
            print(i)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})