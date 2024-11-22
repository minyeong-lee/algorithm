def solution(num_list, n):
    answer = []
    answer = num_list[::n]    
    return answer

print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))