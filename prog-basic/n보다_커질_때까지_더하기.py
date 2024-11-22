def solution(numbers, n):
    answer = 0
    for x in numbers:
        if answer <= n:
            answer += x
        elif answer > n:
            return answer
    return answer

print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))


# 다른 풀이
def solution2(numbers, n):
    answer = 0
    i = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer

print(solution2([34, 5, 71, 29, 100, 34], 123))
print(solution2([58, 44, 27, 10, 100], 139))