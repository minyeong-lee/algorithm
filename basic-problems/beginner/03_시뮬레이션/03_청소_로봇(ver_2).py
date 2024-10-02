# 격자판 밖으로 나가는 경우라면 로봇은 해당 명령 수행하지 않고 무시함
def solution(n, moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    for c in moves:
        for k in range(4):
            if c == dir[k]:
                nx = x + dx[k]  # nx, ny 계산이 경계 조건 만족하지 않아도 항상 계산되기에 불필요한 연산 발생할 수 있음
                ny = y + dy[k]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 경계 체크를 한 번에 모아서 처리하기에 코드가 조금 더 직관적임
            continue  # 조건이 맞지 않는 경우 다음 명령어로 빠르게 넘어가는 것이 명확함
        
        x = nx
        y = ny
    return [x, y]
# 코드 가독성이 좋음 (조건 처리 더 명확함)


# 민영 작성 코드 (2차)
# def solution(n, moves):
#     x = y = 0
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     dir = ['U', 'R', 'D', 'L']
    
#     for c in moves:
#         for k in range(4):
#             if c == dir[k]:
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     x, y = nx, ny    
#                     break  # 불필요한 반복 줄일 수 있음 (큰 입력에서 위의 코드보다 효율적임)
#     return [x, y]


# 민영 작성 코드 (1차)
# def solution(n, moves):
#     x = y = 0
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
    
#     for c in moves:
#         a, b = 0, 0
#         if c == 'U':
#             a = x + dx[0]
#             b = y + dy[0]
#             if a < 0 or b < 0 or a >= n or b >= n:
#                 continue
#             x, y = a, b
#         elif c == 'R':
#             a = x + dx[1]
#             b = y + dy[1]
#             if a < 0 or b < 0 or a >= n or b >= n:
#                 continue
#             x, y = a, b
#         elif c == 'D':
#             a = x + dx[2]
#             b = y + dy[2]
#             if a < 0 or b < 0 or a >= n or b >= n:
#                 continue
#             x, y = a, b
#         elif c == 'L':
#             a = x + dx[3]
#             b = y + dy[3]
#             if a < 0 or b < 0 or a >= n or b >= n:
#                 continue
#             x, y = a, b
#     return [x, y]


print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))