def solution(weight, limit):
    answer = 0
    sumW = 0
    weight.sort()
    for x in weight:
        if sumW + x > limit:  # 현재까지의 총합과 새로운 몸무게를 더한 값이 한도를 넘으면 중단
            break
        sumW += x  # 한도를 넘지 않으면 누적
        answer += 1  # 인원 수 추가
    return answer

# 효율적인 중단, sumW를 미리 계산하지 않고, 바로 조건을 비교하고 나서 누적하는 방식이 더 직관적이며 효율적임


# 민영 작성코드
# def solution(weight, limit):
#     answer = 0
#     std_weight = sorted(weight)
#     sum_weight = 0
#     for x in std_weight:
#         sum_weight = sum_weight + x  # 일단 몸무게를 누적변수에 더한다
#         if sum_weight <= limit:
#             answer += 1
#         else:
#             break
#     return answer

# 비효율적인 조건 검증
# 더하고 나서 검증하기 때문에 불필요한 연산 발생할 수 있고, 첫 번째 코드에 비해 조금 더 장황하게 작성되어 있다

print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))