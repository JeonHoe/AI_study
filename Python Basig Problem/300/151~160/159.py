arr = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in arr:
    if i.split(".")[1] == "h":
        print(i)
        