import heapq
import sys

# 빠른 입출력을 위해 정의
input = sys.stdin.readline

T = int(input())
pq = []
for _ in range(T):
    n = int(input())
    if n == 0:
        if len(pq) == 0:  # 힙에 남은 것이 없다면
            print(0)
        else:  # 힙에 남은 것이 있을때는 출력하기
            print(heapq.heappop(pq)[1])
    else:  # 힙에 값 집어 넣기
        # 여기가 중요한데, 힙큐에 집어넣을 때 절댓값, 그냥값을 튜플로 집어넣으면 우선 절댓값을 비교한 뒤 이후 원래값을 비교한다.
        heapq.heappush(pq, (abs(n), n))

# 다른 해결방법으로는, 음수와 양수일때를 구분하여 각각 분리된 Heap 속에 넣어놓고 각각 값을 비교하는 방법을 통해 구현도 가능하다.