def solution(names):
    answer = []
    for i, v in enumerate(names):
        if i % 5 == 0:
            answer.append(v)
    return answer

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))


# 다른 풀이
def solution2(names):
    return names[::5]
# start와 end를 생략하고 step에 5를 지정한 것
print(solution2(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))
