move_rute = []

def hanoi(count, start, target, assist):
    if count == 1:
        move_rute.append([start, target])
        return None
    hanoi(count-1, start, assist, target)
    move_rute.append([start, target])
    hanoi(count-1, assist, target, start)

user_input = int(input())

hanoi(user_input, "A", "C", "B")
print(move_rute)
print(len(move_rute))
    