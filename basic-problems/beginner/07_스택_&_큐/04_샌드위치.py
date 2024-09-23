# 샌드위치
# nums에서 1-2-1 순이 되면 샌드위치 1개 반환
# 만들 수 있는 샌드위치의 총 개수 answer로 return

def solution(nums):
    answer = 0
    stack = []
    for x in nums:
        if x == 1 and len(stack) >= 2 and stack[-1] == 2 and stack[-2] == 1:
            answer += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(x)
    
    return answer
# for문 안 if문 정도의 복잡성은 괜찮다
# 조건을 더 간결하게 작성하여 조금 더 직관적이고, 실행 속도 면에서 약간의 이점이 있음
# 추가적인 조건 변수를 사용하지 않아 전반적으로 유지보수가 쉽다


# 민영 작성
# def solution(nums):
#     answer = 0
#     stack = []
    
#     for x in nums:
#         if len(stack) > 1:
#             sand = (stack[-1] == 2 and stack[-2] == 1)
#             if x == 1 and sand:
#                 stack.pop()
#                 stack.pop()
#                 answer += 1
#             else:
#                 stack.append(x)
#         else:
#             stack.append(x)
#     return answer
# 조건 변수를 만들어서 다시 한번 확인했지만, 두 번 나누어 체크하여 불필요하게 코드가 늘어났음
# sand 라는 조건 변수로 가독성 높이려는 의도는 좋았지만, 실제로 필요 이상의 코드 길이 유발함


print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))