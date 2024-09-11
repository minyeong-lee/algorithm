def solution(s):
    stack = []
    for x in s:
        if x == '#':
            if len(stack) > 0: # if stack: => 비어있으면 거짓
                stack.pop()
        else:
            stack.append(x)
    return ''.join(stack)


# 민영 작성
# 문자열의 문자를 반복문으로 스택에 저장한다
# '#'을 만나면 pop()
# def solution(s):
#     answer = ""
#     stack = []
#     for x in s:
#         if x == '#':
#             stack.pop()
#         else:
#             stack.append(x)
#     return ''.join(stack)

print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))


"""
    부족했던 점
    - 입력 여부 확인 시 빈 스택일 때 지우면 오류남
"""