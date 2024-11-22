def solution(num_list):
    answer = 0
    odd_sum = 0
    even_sum = 0
    for i, v in enumerate(num_list):
        if i % 2:  # 홀수
            odd_sum += v
        else:
            even_sum += v
    if odd_sum >= even_sum:
        answer = odd_sum
    else:
        answer = even_sum    
    return answer

print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))