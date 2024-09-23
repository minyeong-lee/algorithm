from collections import deque
def BFS(home):
    ch = [0] * 10001   # index가 10000까지이므로
    Q = deque()  # Queue 생성
    Q.append(0)   # 루트 노드 Q에 넣기
    ch[0] = 1    # 첫 번째 노드 넣었을 때 탐색 여부 체크
    L = 0  # 레벨 선언(루트 노드 0레벨부터 시작)\
    while Q:    # Q가 비면 멈춘다
        n = len(Q)
        for i in range(n):  # 한 레벨에서의 탐색 시작
            x = Q.popleft()  # 하나 꺼내서 탐색 시작 -> 이제 하나 꺼내지면, 그의 자식 노드를 만들어서 넣어줘야~!
            if x == home:
                return L  # 레벨이 답이다
            for nx in [x-1, x+1, x+5]:  # 자식을 큐에 넣어줄지 말지(탐색할지 말지 결정함)
                if nx >= 0 and nx <= 10000 and ch[nx] == 0:  # ch (체크value) 로 탐색여부 표시 | 경계선 밖으로 벗어났는지, 이미 탐색했는지 확인
                    Q.append(nx)
                    ch[nx] = 1
        L += 1  # 첫 for문이 끝나야 레벨이 증가한다!


def solution(home):
    answer = BFS(home)    
    return answer


print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))