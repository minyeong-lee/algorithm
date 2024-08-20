from collections import Counter
def solution(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 == 1: # 홀수라면
            odd += 1
    return odd <= 1     # odd = 0 이라면 카운팅 값이 다 짝수라는 의미이므로

    # odd = 0인 경우, odd = 1인 경우 참이 되므로 return 값이 위와 같다

            
            
# 민영 작성 코드
# 짝수일 때 참인 경우 고려하지 못했다.
# def solution(s):
#     answer = False
#     counter = Counter(s)
#     odd_c = 0    
    
#     for x in counter:
#         if counter[x] % 2 != 0:
#             odd_c += 1
#     if odd_c == 1:
#         answer = True   
            
#     return answer
              
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))