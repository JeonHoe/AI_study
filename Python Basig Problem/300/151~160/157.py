arr = ['dog', 'cat', 'parrot']
for i in arr:
    if i[0].islower():
        print(i[0].upper()+i[1:])