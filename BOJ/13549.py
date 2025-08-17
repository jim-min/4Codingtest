# 골드 5, 0-1 BFS

from collections import deque

n, k = map(int, input().split())

max = 100000
time = [max] * (max + 1)

graph = deque()
graph.append(n)
time[n] = 0

while (graph):
    a = graph.popleft()

    if a == k:
        break

    if a*2 <= max and time[a*2] == max:
        graph.appendleft(a*2)
        time[a*2] = time[a]

    if (a-1) >= 0 and time[a-1] == max:
        graph.append(a-1)
        time[a-1] = time[a] + 1

    if (a+1) <= max and time[a+1] == max:
        graph.append(a+1)
        time[a + 1] = time[a] + 1

print(time[k])



