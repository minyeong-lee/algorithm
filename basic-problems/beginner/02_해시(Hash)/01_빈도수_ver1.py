def solution(nums):
    answer = -1
    cnt = [0] * 1001    # 인덱스 번호가 1000까지 있어야 하므로 1001개를 잡아야 함
    
    # Direct-address table 방식의 해싱_빈도 수 카운팅
    # 빈도 수 카운팅
    for x in nums:
        cnt[x] += 1
     
    # 빈도 수가 1인 숫자 중에서 최대값 찾기
    # 아이디어 : 1000부터 돌기 (i가 key 값이기 때문)
    for i in range(1000, 0, -1):    # 1000부터 0까지 1씩 작아지면서 순회
        if cnt[i] == 1:
            return i    # i가 큰 값부터 돌기 때문에 가능함
                        # 최초로 빈도수가 1인 숫자 만나면 그게 바로 빈도수 1인 제일 큰 값
    
    
    # 이 방법은 1부터 1000까지 다 순회하므로 위의 방법 적용하기
    # for i in range(1, 1001):    # 요구사항 준수하여 1부터 시작해도 가능
    #     if cnt[i] == 1:
    #         answer = max(answer, i)
            
    return answer
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))