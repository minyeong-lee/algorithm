def solution(num_list):
    answer = sorted(num_list)[:5]
    return answer

print(solution([12, 4, 15, 46, 38, 1, 14]))

# 문제 내용
# 정수로 이루어진 num_list가 주어짐
# num_list에서 가장 작은 5개의 수 오름차순으로 담은 리스트 return