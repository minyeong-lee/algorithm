def solution(my_string, target):
    answer = 0 
    if target in my_string:
        return 1
    
    return answer

# print(solution("banana", "ana"))
# print(solution("banana", "wxyz"))

# 다른 풀이
def solution2(my_string, target):
    answer = 0

    my_string2 = list(my_string)
    
    for i in range(len(my_string)):
        if my_string2[:len(target)] == list(target):
            return 1
        my_string2.pop(0)
    
    return answer

print(solution2("banana", "ana"))
print(solution2("banana", "wxyz"))


# 문제 내용
# "ana", "ban", "banana", "n" => 문자열 "banana" 의 부분문자열이 맞다
# "aaa", "bnana", "wxyz" => 부분문자열 아님
# target이 my_string의 부분 문자열이라면 1을, 아니라면 0을 return