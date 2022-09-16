per = ["10.31", "", "8.00"]

new_arr = []
  
for i in per:
    try:
        new_arr.append(float(i))
    except:
        new_arr.append(0.0)

print(new_arr)