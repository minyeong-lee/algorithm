from collections import defaultdict
def solution(nums, target):
    answer = [0]*2
    nH = defaultdict(int)   # key의 자료형 int
    for x in nums:  
        y = target - x
        if y in nH:
            return sorted([x, y])
        nH[x] = 1   # 체크 용도. 1은 해당 키가 존재했음을 의미    
       
    return answer


# 민영 작성 코드
# def solution(nums, target):
#     answer = [0]*2
#     hL = defaultdict(int)
#     for x in nums:
#         hL[x] = target - x
        
#     for val in hL.values():
#         if val in hL:
#             answer = [val, target-val]
    
#     answer.sort()
#     return answer                            
            
                
print(solution([3, 7, 2, 12, 9, 15, 8], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))

