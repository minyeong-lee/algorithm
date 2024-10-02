def solution(moves):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x = y = 0
    d = 1  # 방향 의미 (보고 있는 방향) | d값은 dx, dy의 index 값 | 초기값은 3시 방향 1로 초기화
    for c in moves:
        if c == 'G':
            x = x + dx[d]  # 격자 밖으로 나가지 않는다는 요구사항으로 x에 바로 대입 가능
            y = y + dy[d]  # d는 로봇이 보고 있는 방향
        elif c == 'R':
            # d = d + 1   # 이게 안되는 이유는 인덱스가 0 ~ 3 이므로
            d = (d + 1) % 4  # 로봇이 보고 있는 방향 바꿔줌
        elif c == 'L':
            # d = d - 1  
            d = (d + 3) % 4  # 다른 언어에서 이렇게 나머지를 구함 | d-1해서 구한 나머지와, d+3해서 구한 나머지는 동일함
    return [x, y]

print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))  
    
    
# 민영 작성코드
# def solution(moves):
#     x = y = 0
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     sight = [0, 1, 0, 0]
      
    
#     for c in moves: # 'GGGRGGG' 라는 문자열 순회
#         # c가 'G'인 경우, 이전에 있던 방향에서 +1
#         for k in range(4):
#             if c == 'G' and sight[k] == 1:
#                 nx = x + dx[k]  # nx = 0 + 0
#                 ny = y + dy[k]  # ny = 2 + 1
#                 print(f'c == "G"일 때의 nx : {nx}, ny : {ny} 는 얼마일까용')
#                 if 0 <= nx < 4 and 0 <= ny < 4:
#                     x, y = nx, ny
#             elif c == 'R' and sight[k] == 1:
#                 sight[k] = 0
#                 if k == 3:
#                     sight[0] = 1
#                     continue
#                 sight[k+1] = 1
#             elif c == 'L' and sight[k] == 1:
#                 sight[k] = 0
#                 if k == 0:
#                     sight[-1] = 1
#                     continue
#                 sight[k-1] = 1
#     return [x, y]


# print(solution('GGGRGGG'))

# 4방향 탐색으로 보는데, 현재 바라보는 방향을 어떻게 구별할 수 있을까?
