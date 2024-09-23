# 스택을 사용하여 연속된 문자를 처리하는 방식
def solution(s):
    stack = []
    for x in s:
        if stack and stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    return ''.join(stack)
    """
        - 코드가 간결하고 조건문을 한번만 사용함
        - if stack 은 스택이 비어 있지 않을 때만 참
    """

# 민영 작성코드
# def solution(s):
#     stack = [s[0]]

#     for i in range(1, len(s)):
#         if len(stack) != 0:
#             if s[i] == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(s[i])
#         else:
#             stack.append(s[i])

#     return ''.join(stack)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))

# 조건문에서 'stack' 자체는 비어 있으면 거짓이고, 무언가 있으면 참이다 (파이썬답고, 일반적이며 효율적인 방식)
# 이는 파이썬에서 빈 리스트는 False 로 평가되기 때문에 가능하다

stack = []
if stack and stack[-1] == x:
    stack.pop()