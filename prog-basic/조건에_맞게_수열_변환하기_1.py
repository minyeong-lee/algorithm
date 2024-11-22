def solution(arr):
    answer = []
    for i, val in enumerate(arr):
        if val >= 50 and val % 2 == 0:
            answer.append(val // 2)
        elif val < 50 and val % 2 != 0:
            answer.append(val * 2)
        else:
            answer.append(val)
    return answer

print(solution([1, 2, 3, 100, 99, 98]))


# 다른 풀이
def solution2(arr):
    answer = []
    
    for item in arr:
        if item >= 50 and not item % 2:
            answer.append(item // 2)
        elif item < 50 and item % 2:
            answer.append(item * 2)
        else:
            answer.append(item)
        
    return answer

print(solution2([1, 2, 3, 100, 99, 98]))            