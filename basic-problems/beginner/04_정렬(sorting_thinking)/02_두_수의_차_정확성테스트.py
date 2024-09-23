# O(n^2)
def solution(nums):
    answer = []
    n = len(nums)
    minN = 1000000000
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if diff < minN:
                minN = diff
    
    for i in range(n):
        for j in range(i+1, n):
            diff = abs(nums[i] - nums[j])
            if diff == minN:
                answer.append(sorted([nums[i], nums[j]]))
    
    return answer

# 민영 작성 코드
# 차이가 최소일 때마다 쌍을 추가하지만, 차이가 같은 경우에도 무조건 추가하고,
# 나중에 불필요한 쌍을 제거하는 방식임
# 마지막에 조건을 확인하면서 필요 없는 쌍을 제거하고 있는 것이 불필요한 반복을 야기할 수 있음
# 요소 추가와 제거가 반복되며 성능 면에서 비효율적일 수 있음

# def solution(nums):
#     answer = []
#     minN = 10000
#     nums.sort()
        
#     for i in range(1, len(nums)):
#         gap = nums[i] - nums[i-1]
#         if gap < minN:
#             answer.append([nums[i-1], nums[i]])
#             minN = gap
#         elif gap == minN:
#             answer.append([nums[i-1], nums[i]])
        
#     for x in answer:
#         if x[1] - x[0] != minN:
#             answer.remove(x)
#     return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
