from math import prod
def solution(num_list):
    answer = 0
    N = len(num_list)
    if N >= 11:
        answer = sum(num_list)
    else:
        answer = prod(num_list)
    return answer

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))


# 다른 풀이
def solution2(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)

print(solution2([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution2([2, 3, 4, 5]))