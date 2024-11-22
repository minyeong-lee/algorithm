def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    if pat in myString:
        return 1
    return answer

print(solution("AbCdEfG", "aBc"))
print(solution("aaAA", "aaaaa"))


# 다른 풀이
def solution2(myString, pat):
    return int(pat.lower() in myString.lower())

print(solution2("AbCdEfG", "aBc"))
print(solution2("aaAA", "aaaaa"))