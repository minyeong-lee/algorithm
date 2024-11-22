def solution(strArr):
    answer = []

    for i in range(len(strArr)):
        if i % 2: # 나머지가 1이면 참. 즉 홀수이면
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
    return answer

print(solution(["AAA","BBB","CCC","DDD"]))
print(solution(["aBc","AbC"]))

# 개선
# range 보다 enumerate 를 사용하여 index 사용 권장
def solution2(strArr):
    answer = []
    for i, val in enumerate(strArr):
        if i%2: answer.append(val.upper())
        else: answer.append(val.lower())
    return answer

print(solution2(["AAA","BBB","CCC","DDD"]))
print(solution2(["aBc","AbC"]))
