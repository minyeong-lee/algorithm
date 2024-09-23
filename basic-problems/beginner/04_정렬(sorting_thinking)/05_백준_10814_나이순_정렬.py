import sys
input = sys.stdin.readline

def solution(people):
    people.sort(key = lambda v : v[0])
    
    result = []
    for x in people:
        result.append(f'{x[0]} {x[1]}')
    
    return '\n'.join(result)    

N = int(input().strip())
people = []
for i in range(N):
    age, name = input().strip().split()  # 입력받은 값을 분리
    people.append([int(age), name])  # 나이는 int로 변환, 이름은 문자열 그대로
print(solution(people))


# 다른 코드
# def solution(member):
#     member.sort(key = lambda v : (v[0]))
#     for x in member:
#         print(x[0], x[1])

# n = int(input())
# arr = []
# for i in range(n):
#     a, b = input().split()
#     a = int(a)
#     arr.append([a, b])
# solution(arr)

