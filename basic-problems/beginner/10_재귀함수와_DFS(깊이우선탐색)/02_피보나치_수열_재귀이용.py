# 재귀함수로 풀이
# n에 구해야 할 피보나치 수열의 항 번호가 주어지면
# 피보나치 수열의 n번째 항을 구해 return
def DFS(n):
    if n <= 2:
        return 1
    
    arr = [1,1]
    for i in range(n-2):
        arr.append(arr[-2] + arr[-1])
    return arr[n-1]

print(DFS(10))