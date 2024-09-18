# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def DFS(x, y, board):
    board[x][y] = 0  # 방문한 건 0으로 바꿈
    for k in range(4):  # 4방향 탐색
        # nx = x + dx[k]  # nx 는 가려고 하는 지점 | k=0이면 12시 방향으로 가는 것
        # ny = y + dy[k]
        dx, dy = d[k]
        nx = x + dx
        ny = y + dy
        
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:  # 그 지점이 검정색이면 호출이 일어남 (새로운 좌표가 범위 안에 있고, 검정색(1)이면)
            DFS(nx, ny, board)
            

def solution(board):
    answer = 0   # 영역의 개수
    for i in range(5):  # 5 * 5 배열만 들어온다고 했으니까
        for j in range(5):
            if board[i][j] == 1:  # 최초로 1이 발견되면
                answer += 1  # 아 영역 하나 발견되었다! 하고
                DFS(i, j, board)  # 그 지점부터 퍼져나감 | 현재 board는 solution() 함수의 지역변수이므로 매개변수로 넘겨줘야 함
    
    
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))