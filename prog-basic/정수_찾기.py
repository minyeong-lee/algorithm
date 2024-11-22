def solution(num_list, n):
    answer = 0
    
    for x in num_list:
        if x == n:
            return 1        
    
    return answer


print(solution([1, 2, 3, 4, 5], 3))
print(solution([15, 98, 23, 2, 15], 20))

# 문제 내용
# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때,
# num_list 안에 n이 있으면 1을 없으면 0을 return 하기


# 다른 사람 풀이
def solution2(num_list, n):
    return int(n in num_list)  # False = 0, True = 1

def solution3(num_list, n):
    return 1 if n in num_list else 0