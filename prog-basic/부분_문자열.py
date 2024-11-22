def solution(str1, str2):
    answer = 0
    n1 = len(str1)
    n2 = len(str2)
    cnt = 0
    
    for i in range(n2-n1+1):
        if str1[0] != str2[i]:
            continue
        cnt = 1
        sc_str = str2[i:i+n1]
        # for j in range(n1-1):
        #     if str1[j+1] != sc_str[j+1]:
        #         break
        #     cnt += 1    
        if sc_str == str1:
            return 1       
    
    return 0

# print(solution("abc", "aabcc"))
# print(solution("tbt", "tbbttb"))



# 문제 내용
# 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 함
# 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열임

# 문자열 str1, str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을
# 부분 문자열이 아니라면 0을 return하라