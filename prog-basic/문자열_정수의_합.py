def solution(num_str):
    answer = 0
    num_str = list(map(int, num_str))
    for x in num_str:
        if x == 0:
            continue
        answer += x
    return answer

print(solution("123456789"))
print(solution("1000000"))

# 다른 풀이
def solution2(num_str):
    return sum(map(int, num_str))

print(solution2("123456789"))
print(solution2("1000000"))
# map 함수는 주어진 함수를 반복 가능한 객체(iterable)의 모든 항목에 적용하고, 결과 반환함
# 여기서 문자열도 시퀀스이기에 당연히 반복 가능한 객체이며, 그래서 각 문자에 대해 int 함수 적용 가능


# 문제 내용
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때,
# 각 자리수의 합을 return