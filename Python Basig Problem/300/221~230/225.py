def print_value_by_key(dict1, key):
    if type(dict1) is dict:
        if key in list(dict1.keys()):
            res = dict1[key]
    print(res)


my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print_value_by_key  (my_dict, "10/26")
        