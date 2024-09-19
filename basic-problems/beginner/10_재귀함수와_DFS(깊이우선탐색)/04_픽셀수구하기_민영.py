# 매개변수 board에 모니터 화면의 격자정보가 주어지면
# 검정색으로 칠해진 각 영역의 픽셀수를 순서대로 배열에 담아 반환하기
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 0

def DFS(x, y, board):
    global cnt
    board[x][y] = 0  # 방문한 지점 체크
    for k in range(4):
        dx, dy = d[k]
        nx = x + dx
        ny = y + dy
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board[nx][ny] == 1:
            cnt += 1
            DFS(nx, ny, board)
            

def solution(board):
    global cnt
    answer = []  # 픽셀 수 모음
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                cnt = 0
                cnt += 1    # 잊을 우려가 있음
                DFS(i, j, board)
                answer.append(cnt)
                # cnt = 0

    return answer

print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))


"""
정환's 코드 리뷰
- 강의 코드랑 비교했을 때 cnt += 1 하는 부분이 2번이지만, 괜찮다
- 단, 처음 재귀 호출 전에 cnt를 추가하는 부분이 잊을 우려가 있어서 조심해야 한다
- cnt를 0으로 초기화하는 부분을 전 / 후에 하는 것은 상관없다. 
- 안 좋은 코드는 아니다!
"""