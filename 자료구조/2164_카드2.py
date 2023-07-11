from collections import deque

T = int(input())

# 한번 버리고 한번 제일 아래로.
# 제일 아래로 간다는 것은 first in first out 이니까 queue 일것 같음

arr = deque()
for i in range (T):
    arr.append(i + 1)
# print(arr)
i = 0
while len(arr) > 1:
    if i % 2 == 0 :
        arr.popleft()
        # print(arr)
    elif i % 2 == 1:
        n = arr.popleft()
        # print(n)
        arr.append(n)
        # print(arr)

    i += 1
print(arr[0])