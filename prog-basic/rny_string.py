def solution(rny_string):
    answer = []
    if 'm' not in rny_string:
        return rny_string
    for x in rny_string:
        if x == 'm':
            answer.append('rn')
        else:
            answer.append(x)
    return ''.join(answer) 

print(solution("masterpiece"))

# 다른 풀이
def solution2(rny_string):
    return rny_string.replace('m', 'rn')