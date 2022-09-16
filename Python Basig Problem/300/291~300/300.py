per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(float(0))
    else:
        print("data exist")
    finally:
        print("changed clear")