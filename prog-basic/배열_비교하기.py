def solution(arr1, arr2):
    N1, N2 = len(arr1), len(arr2)

    if N1 != N2:
        if N1 > N2:
            return 1
        elif N1 < N2:
            return -1
        return 0
    
    if sum(arr1) > sum(arr2):
        return 1
    elif sum(arr1) < sum(arr2):
        return -1
    else:
        return 0

print(solution([49, 13], [70, 11, 2]))
print(solution([100, 17, 84, 1]	, [55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))