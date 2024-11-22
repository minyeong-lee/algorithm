def solution(num_list):
    answer = -1
    for i, x in enumerate(num_list):
        if x < 0:
            return i
    return answer

print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))

# 다른 풀이
def solution2(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0: return i
    return -1