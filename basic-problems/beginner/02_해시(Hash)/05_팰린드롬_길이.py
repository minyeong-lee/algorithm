from collections import Counter
def solution(s):
    sH = Counter(s)
    odd = 0     # 홀수의 개수
    for key in sH:
        if sH[key] % 2 == 1:    # 값이(갯수가) 홀수인 경우
            odd += 1
    
    return len(s) - odd + 1 if odd > 0 else len(s)   
    
    
# 민영 작성 코드
# def solution(s):
#     answer = 0  # 길이
#     sH = Counter(s)
#     sL = 0  # 홀수 구분자
    
#     for key in sH:
#         if sH[key] % 2 == 0:
#             answer += sH[key]
#         elif sH[key] % 2 != 0:
#             if sL == 0:  # 첫 홀수의 경우
#                 answer += sH[key]
#                 sL = 1
#             else:   # 나머지 홀수의 경우
#                 answer += (sH[key] - 1)

#     return answer

                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))