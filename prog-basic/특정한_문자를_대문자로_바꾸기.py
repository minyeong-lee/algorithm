def solution(my_string, alp):
    answer = ''
    my_string = list(my_string)
    
    if alp not in my_string:
        return ''.join(my_string)
    
    for i in range(len(my_string)):
        if my_string[i] == alp:
            my_string[i] = my_string[i].upper()
    answer = ''.join(my_string)
    return answer

print(solution("programmers", "p"))
print(solution("lowercase", "x"))


# 다른 풀이
def solution2(my_string, alp):
    return my_string.replace(alp, alp.upper())

print(solution2("programmers", "p"))
print(solution2("lowercase", "x"))