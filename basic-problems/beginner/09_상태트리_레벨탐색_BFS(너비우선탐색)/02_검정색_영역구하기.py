from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x, y, board):
    Q = deque()
    Q.append([x, y])
    board[x][y] = 0
    L = 0
    while Q:
        n = len(Q)
        for i in range(n):
            x, y = Q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if(nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1):
                    Q.append([nx, ny])
                    board[nx][ny] = 0
        L += 1  # BFS는 고급 문제일수록 레벨 이용하여 문제 풀이 많이 진행하기에 항상 Level은 만들자

def solution(board):
    answer = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:  # 검정색 영역 발견되면
                answer += 1
                BFS(i, j, board)
                
    
    return answer


print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))