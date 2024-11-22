# 정수배열 arr과 자연수 k가 주어진다
# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더한다
# 이러한 변환을 마친 후의 arr를 return 하는 solution 함수 완성하기

# 민영 작성코드
def solution(arr, k):
    answer = []
    
    if (k % 2 == 0):
        for x in arr:
            answer.append(x + k)
    else:
        for x in arr:
            answer.append(x * k)
    
    return answer



