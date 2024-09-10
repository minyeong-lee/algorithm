from collections import Counter
from collections import defaultdict, Counter
# 정답 코드
# 'completion'리스트의 값을 'sH'에서 빼는 방식
# 메모리 사용량이 더 적고, 좀 더 효율적임
def solution(participant, completion):
    answer = ''
    sH = Counter(participant)
    for x in completion:
        sH[x] -= 1
    for key in sH:
        if sH[key] == 1:
            return key
    return answer


# 민영 작성 코드
# 2개의 Counter 객체를 만들어 비교하는 방식
# def solution(participant, completion):
#     answer = ''
#     ptc_dict = Counter(participant)
#     cpt_dict = Counter(completion)

#     for name in ptc_dict:
#         if ptc_dict[name] != cpt_dict[name]:
#             answer = name
#     return answer

n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n-1):
    b.append(input())
print(solution(a, b))
