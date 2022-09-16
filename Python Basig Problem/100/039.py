string = input()

if string.find("q") or string.find("b"):
    string=string.replace('q','e')
    string=string.replace('b','n')
print(string)