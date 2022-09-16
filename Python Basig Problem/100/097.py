from sqlite3 import Time


def solution(n,l):
    answer = 0
    man = [0]*n
    while sum(l)!=0:
				#택배원 수 만큼 반복
        for j in range(len(man)):
						# 택배원이 배달하고있는 택배의 잔여거리가 0인경우(배송완료인경우) 택배상차
            if man[j] == 0 and l:
                man[j]+=l.pop(0)
				#택배원들 배송거리 -1 처리
        man = list(map(lambda x : x-1,man))
				# 1회 반복단 1의 시간증가
        answer+=1
		# 남은 택배 잔여거리중 가장 많은 시간이 남은 택배를 더해줌
    answer+=max(man)
    return answer

human = 3
time = [1,2,1,3,3,3]


print(solution(human, time))
# 출력값 = 5