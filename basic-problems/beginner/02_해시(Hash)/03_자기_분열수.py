from collections import Counter
def solution(nums):
    answer = 1000000000
    nH = Counter(nums)
    for key in nH:
        if nH[key] == key:
            answer = min(answer, key)
    return -1 if answer == 1000000000 else answer   # 다른 변수 두지 않고 조건문 활용

# 민영 작성
# def solution(nums):
#     answer = -1
#     min_key = 1000000

#     nH = Counter(nums)
#     for key in nH:        
#         if key == nH[key]:
#             min_key = min(min_key, key)
#             answer = min_key
    
#     return answer
                
print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))