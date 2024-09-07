def solution(nums):
    n = len(nums)
    cnt = 1     # 사탕의 종류(중복 제거하고 남은 숫자의 개수)
    nums.sort()
    for i in range(1, n):
        if nums[i-1] != nums[i]:
            cnt += 1
    
    return cnt if cnt < n//2 else n//2

# 민영 작성 코드
# def solution(nums):
#     answer = 1
#     n = len(nums)
#     nums = sorted(nums)

#     for i in range(1, n):
#         if nums[i] != nums[i-1]:
#             answer += 1
#     answer = min(answer, n//2)
#     return answer


print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))