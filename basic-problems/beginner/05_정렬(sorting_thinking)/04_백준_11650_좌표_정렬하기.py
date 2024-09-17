import sys
input = sys.stdin.readline

def solution(N, points):
    points.sort(key = lambda v : (v[0], v[1]))
    
    result = []
    for i in range(N):
        result.append(f'{points[i][0]} {points[i][1]}')
    
    return '\n'.join(result)
        
        
N = int(input().strip())
points = []
for i in range(N):
    x_y = list(map(int, input().strip().split()))
    points.append(x_y)

print(solution(N, points))