# def DFS(n):
#     if n == 0:
#         return
#     else:
#         print(n, end=' ')
#         DFS(n-1)   
    
# DFS(5)  # 5 4 3 2 1

def DFS(n):
    if n == 0:
        return
    else:
        DFS(n-1)
        print(n, end=' ')

DFS(5)  # 1 2 3 4 5

# 스택이라는 자료구조를 사용하기 때문에
# 위의 두 경우에서 출력이 다르다!
