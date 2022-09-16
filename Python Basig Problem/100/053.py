def sol(string):

    arr1 = ["{", "[", "("]
    arr2 = ["}", "]", ")"]

    list1 = []
    list2 = []

    for ch in string:
        if ch in arr1:
            list1.append(ch)
        elif ch in arr2:
            list2.append(ch)
    
    if len(list1) != len(list2):
        print("NO")
    else:
        for i in range(len(list1)):
            if list1[i] == "{" and list2[-i-1] == "}":
                pass
            elif list1[i] == "[" and list2[-i-1] == "]":
                pass
            elif list1[i] == "(" and list2[-i-1] == ")":
                pass
            else:
                print("NO")
                break
            if i == len(list1)-1:
                print("YES")
    
str1 = input()
sol(str1)

