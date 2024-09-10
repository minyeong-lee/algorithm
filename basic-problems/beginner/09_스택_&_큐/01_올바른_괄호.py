# 올바른 괄호
# 괄호 문자열이 입력되면 올바른 괄호이면 "YES", 올바르지 않으면 "NO"를 출력한다
def solution(s):
    answer = "YES"
    stack = []
    for x in s:
        if x == ')':
            if len(stack) == 0:
                return "NO"
            stack.pop()
        else:   # '(' 입력되는 경우
            stack.append(x)
            
    if len(stack) > 0:
        return "NO"   
    
    return answer

# 민영 작성코드

# 아이디어
# 스택을 만들어서 괄호를 하나씩 담고, 오른쪽 괄호 짝을 만나면 pop한다
# 위의 과정을 반복했을 때, 스택에 괄호가 남아있거나, pop할 짝이 스택에 없으면 올바르지 않은 것으로 간주한다
# def solution(s):
#     stack = []
#     if len(s) % 2 != 0:
#         return "NO"
#     for i in range(len(s)):
#         if s[i] == '(':
#             stack.append('(')
#         elif s[i] == ')':
#             if len(stack) == 0:
#                 return "NO"
#             stack.pop()
#     if len(stack) == 0:
#         return "YES"
#     return "NO"

print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
