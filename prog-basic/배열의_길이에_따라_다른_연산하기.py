def solution(arr, n):
    answer = []
    l = len(arr)
    if (l % 2 != 0): 
        for i in range(l):
            if (i == 0 or i % 2 == 0):
                arr[i] += n
    else:
        for i in range(l):
            if i % 2 != 0:
                arr[i] += n
    answer = arr
    return answer

print(solution([49, 12, 100, 276, 33], 27))
print(solution([444, 555, 666, 777], 100))


# 다른 풀이
def solution2(arr, n):
    N = len(arr)
    if N%2:  # 결과가 1일 때 True => 즉, 홀수이면
        for i in range(0,N,2): arr[i]+=n  # 0부터 시작해서 2씩 증가하는 숫자들을 생성함 (짝수 인덱스 요소만 반복 처리)
    else:
        for i in range(1,N,2): arr[i]+=n
    return arr

# range(start, stop, step) 형태 => start는 시작 값, stop은 종료 값, step은 증가 간격