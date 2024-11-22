def solution(todo_list, finished):
    answer = []
    todo_dict = dict(zip(todo_list, finished))        
    for k, v in todo_dict.items():
        if v == False: answer.append(k)
    return answer

print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]))


# 다른 풀이
def solution2(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]
# 리스트 컴프리헨션 : 조건에 맞는 요소들을 직접 리스트로 만들어 줌

# not b
# not b 는 b가 False일 때 True로 평가되어 조건 만족함

# 아래와 같은 표현임
# for x, b in zip(todo_list, finished):
#     if not b:
#         answer.append(x)
# return answer