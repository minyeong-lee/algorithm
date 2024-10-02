def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    for c in moves:
        for k in range(4):
            if c == dir[k]:
                x = x + dx[k]
                y = y + dy[k]
    return [x, y]


print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))

# 문제 조건에서 '격자판 밖으로 벗어나는 명령은 주어지지 않는다'라고 명시되어 있기에
# x = x + dx[k] 라고 바로 이동해도 되는 것


