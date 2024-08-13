def solution(nums):
    answer = 0
    longN = 0
    
    for x in nums:
        if x == 1:
            longN += 1
        else:
            answer = max(answer, longN)
            longN = 0
    
    answer = max(answer, longN)
    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))