def solution(n_str):
    answer = int(n_str)
    
    return str(answer)

print(solution("0010"))
print(solution("854020"))


# 다른 풀이
def solution2(n_str):
    return n_str.lstrip('0')

print(solution2("0010"))
print(solution2("854020"))

# 문제 내용
# 정수로 이루어진 문자열 n_str이 주어질 때,
# n_str 의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return