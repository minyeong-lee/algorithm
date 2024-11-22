def solution(myString):
    answer = ''
    ch = 'a'
    
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == ch:
            myString[i] = myString[i].upper()
        elif myString[i] == ch.upper():
            continue
        else:
            myString[i] = myString[i].lower()
    answer = ''.join(myString)    
    return answer

print(solution("abstract algebra"))
print(solution("PrOgRaMmErS"))


# 다른 풀이
def solution2(myString):
    return myString.lower().replace('a', 'A')

print(solution2("abstract algebra"))
print(solution2("PrOgRaMmErS"))
