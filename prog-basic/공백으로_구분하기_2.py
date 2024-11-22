def solution(my_string):
    answer = []
    temp = ''
    my_string = list(my_string.strip())
    
    for i in range(len(my_string)):
        if my_string[i] == ' ':
            if my_string[i-1] != ' ':
                answer.append(temp)
                temp = ''
            continue
        temp += my_string[i]
        if i == len(my_string)-1:
            answer.append(temp)
                
    return answer

print(solution(" i    love  you"))
print(solution("    programmers  "))