def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        N = arr[i]
        for j in range(N): 
            answer.append(arr[i])
    
    return answer

print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))


# 다른 풀이
def solution2(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer
