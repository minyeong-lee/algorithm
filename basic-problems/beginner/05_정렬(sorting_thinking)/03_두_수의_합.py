# 투 포인터 알고리즘
# 1차원 배열에서 각자 다른 원소를 가리키고 있는 
# 2개의 포인터를 조작해가면서 원하는 값을 찾을 때까지 탐색하는 알고리즘
# O(n^2)가 걸리는 문제를 O(n)에 해결할 수 있다
def solution(nums, target):
    answer = [0] * 2
    nums.sort()
    left = 0
    right = len(nums) - 1
    
    # 이 조건에 대해서 진행과정을 생각해보기. 
    while left < right: # 지금의 경우, 점점 좁혀들어가고 left와 right가 같은 수가 되지 않음 (그 경우 볼 필요 없음)
        sumN = nums[left] + nums[right]
        if sumN == target:
            return [nums[left], nums[right]]
        if sumN < target:
            left += 1
        else:
            right -= 1  
    return answer


# 민영 작성 코드
# def solution(nums, target):
#     answer = []
#     nums.sort()
    
#     for i in range(len(nums)):
#         mN = target - nums[i]
#         if mN in nums:
#             tL = [nums[i], mN]
#             answer.append(tL)
#             return answer[0]           
#     return [0,0] if answer == [] else answer[0]


print(solution([7, 3, 2, 13, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))