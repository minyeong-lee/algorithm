# 시뮬레이션
# 작은 의미로는 문제가 제시한 규칙에 따라 개체를 이동시키는 알고리즘
# 큰 의미로는 문제가 요구하는 대로 시행되도록 코드를 구현하는 알고리즘

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
nums = []

for i in range(5):
    for j in range(5):
        for k in range(4):
            nx = i + dx[i]
            ny = j + dy[j]
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
                if nums[nx][ny] <= nums[i][j]:
                    flag = False