def ff(s):
    k = ""
    if type(s) is str:
        s = s.replace(" ", "")
        s = s.replace(".", "")
        k = s[::]
    k = k[::-1]
   
    if s == k:
        return True
    else:
        return False


if __name__ == "__main__":
    str1 = input("")
    print(ff(str1))