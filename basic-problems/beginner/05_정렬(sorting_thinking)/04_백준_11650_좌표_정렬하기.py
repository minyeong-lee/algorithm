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


# 정답 코드
# def solution(nums):
#     nums.sort(key = lambda v : (v[0], v[1]))
#     for x in nums:
#         print(x[0], x[1])


# n = int(input())
# arr = []
# for i in range(n):
#     a, b = map(int, input().split())  # 각 입력 값을 map을 통해 정수로 변환함
#     arr.append([a, b])    #변환된 값을 [a, b] 형태로 리스트에 저장함
# solution(arr)