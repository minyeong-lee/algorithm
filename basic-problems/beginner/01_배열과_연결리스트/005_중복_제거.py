from collections import deque
def solution(nums):
    answer = deque()
    answer.appendleft(nums[0])
    
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            answer.appendleft(nums[i])
    
    return list(answer)

# range(start, stop) 시작위치 지정 가능


# 보완 전 코드
# from collections import deque
# def solution(nums):
#     answer = deque()
#     answer.append(nums[0])
#     n = len(nums)
    
#     for i in range(n-1):
#         if nums[i+1] != nums[i]:
#             answer.appendleft(nums[i+1])
           
#     return list(answer)
    
   
print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))