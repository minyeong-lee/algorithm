def solution(num_list):
    answer = []
    num_list.sort()
    answer = num_list[5:]
    return answer

# print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))


# 다른 풀이
def solution2(num_list):
    return sorted(num_list)[5:]

print(solution2([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))

# 문제 내용
# 정수로 이루어진 num_list가 주어짐
# num_list에서 가장 작은 5개의 수를 제외한 수들을 제외한 나머지 원소들을 오름차순으로 담은 리스트 return