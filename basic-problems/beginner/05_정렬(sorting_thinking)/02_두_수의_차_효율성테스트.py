# O(n log n) 정렬
# O(n)
# 최종적으로 더 큰 시간복잡도인 O(n log n)
# 정렬하고 두 수의 차이 고려 (앞에만 비교하기)
def solution(nums):
    answer = []
    n = len(nums)
    minN = 1000000000
    nums.sort()     # O(n log n)
    for i in range(1, n):           # O(n)
        diff = nums[i] - nums[i-1]
        minN = min(minN, diff)
        # 한번에 최소의 차이를 구함
    
    for i in range(1, n):           # O(n)
        diff = nums[i] - nums[i-1]
        if diff == minN:    # 그 최솟값과 일치하는 쌍만 추가하여 효율적임
            answer.append([nums[i-1], nums[i]])

    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))