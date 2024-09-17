# 고장난 프린터
# 먼저 2개의 작업을 프린터하고, 3번째 작업은 맨 뒤로 보낸다
# 맨 마지막에 출력되는 작업의 번호를 반환한다

from collections import deque
def solution(nums):
    queue = deque(nums)
    while queue:    # queue가 빈 자료구조이면 거짓이라 멈춤
        for _ in range(2):
            if len(queue) >= 2:
                queue.popleft()
        queue.append(queue.popleft())
        if len(queue) == 1:
            return queue[0]


# 민영 작성 코드
# def solution(nums):
#     queue = deque(nums)    
#     while True:
#         queue.popleft()
#         queue.popleft()
#         third_num = queue.popleft()
#         queue.append(third_num)       
#         if len(queue) <= 2:
#             return queue[-1]

"""
    [보완할 점]
    - while True 무한 루프는 명확한 종료 조건이 있거나,
    특정 이벤트를 기다리는 경우 사용하면 유용함 (종료 조건이 불확실한 경우는 주의해야 함)
    
    - 지금의 경우, while deque 가 더 적절함 (큐가 비어갈 때까지 반복하는 구조)
"""      

# 또 다른 코드 제안
# def solution(nums):
#     queue = deque(nums)
#     while len(queue) > 2:
#         queue.popleft()
#         queue.popleft()
#         queue.append(queue.popleft())
#     return queue[-1]  # 큐에 2개 이하의 작업만 남았을 때, 맨 오른쪽에 있는 요소 반환함


print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))