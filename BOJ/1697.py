# DP로 풀려고 했는데 자꾸 50%에서 안 돼서 BFS로 함

from collections import deque

a, b = map(int, input().split())
time = [float('inf')] * 100001

time[a] = 0
queue = deque()
queue.append(a)

while queue:
    key = queue.popleft()

    if (key == b):
        break

    for i in [key + 1, key - 1, key * 2]:
        if 0 <= i < 100001 and time[i] > time[key] + 1:
            queue.append(i)
            time[i] = time[key] + 1

print(time[b])

