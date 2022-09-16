N = int(input("도장 크기:"))
stmp = []
print("도장 :")
for i in range(N):
    stmp.append(list(map(int,input().split(' '))))
k = int(input("회전:"))


def solution(stmp,n):
    N = len(stmp)
    p = [[0] * N for _ in range(N)]
    
    p = sum_matrix(p,stmp)
    for i in range(n):
        stmp = rotate(stmp)
        p=sum_matrix(p,stmp)
    return p


def rotate(stmp):
    N = len(stmp)
    rot = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = stmp[i][j]
    return rot


def sum_matrix(p,stmp):
    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i][j] = p[i][j]+stmp[i][j]
    return p

print(solution(stmp,k))