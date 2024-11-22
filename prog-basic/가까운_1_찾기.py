def solution(arr, idx):
    answer = -1
    if 1 in arr[idx:]:
        for i, x in enumerate(arr[idx:]):
            if x == 1:
                return idx+i
    return answer

print(solution([0, 0, 0, 1], 1))
print(solution([1, 0, 0, 1, 0, 0], 4))
print(solution([1, 1, 1, 1, 0], 3))

# 다른 풀이
def solution2(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1
    return answer

# index 메서드
# 리스트나 문자열에서 특정 값이 처음으로 나타나는 위치(인덱스)를 찾아 반환함
# 기본적으로 왼쪽에서 오른쪽으로 탐색하여 가장 먼저 발견된 인덱스 반환
# 만약 찾는 값이 리스트에 없다면 ValueError 예외 발생시킴
# 두 번째 인자는 시작 인덱스