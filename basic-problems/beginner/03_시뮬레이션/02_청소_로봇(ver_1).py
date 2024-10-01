# 청소 로봇은 이차원 배열 0행 0열에서 시작하여 움직인다
# 행과 열의 길이는 정해져 있지 않다

def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for c in moves:
        if c == 'U':
            x = x + dx[0]
            y = y + dy[0]
        elif c == 'R':
            x = x + dx[1]
            y = y + dy[1]
        elif c == 'D':
            x = x + dx[2]
            y = y + dy[2]
        elif c == 'L':
            x = x + dx[3]
            y = y + dy[3]
    return [x, y]


# 민영 작성 코드
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def solution(moves):
#     x = y = 0
#     n = len(moves)
    
#     for i in range(n):
#         if moves[i] == 'U':
#             x += dx[0]
#             y += dy[0]
#         elif moves[i] == 'R':
#             x += dx[1]
#             y += dy[1]
#         elif moves[i] == 'D':
#             x += dx[2]
#             y += dy[2]
#         elif moves[i] == 'L':
#             x += dx[3]
#             y += dy[3]
    
#     return [x, y]

print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
