string = input()
word = input()

if string.find(word) != -1:
    print(string.index(word))
else:
    print("Word does not exist in String")
