# 재귀함수로 풀이
# n에 구해야 할 피보나치 수열의 항 번호가 주어지면
# 피보나치 수열의 n번째 항을 구해 return
# 1 1 2 3 5 8 13 21 34
def DFS(n):
    if n == 1 or n == 2:  # 더 직관적인 표현
        return 1
    else:  # else문은 논리적 흐름을 명확히 하기 위해 사용하는 것이 좋음
        return DFS(n-2) + DFS(n-1)

# def DFS(n):
#     if n <= 2:   # 의미가 덜 명확함
#         return 1
    
#     return DFS(n-2) + DFS(n-1)

print(DFS(5))
print(DFS(6))
print(DFS(7))
print(DFS(8))
print(DFS(9))