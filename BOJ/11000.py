import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    q.append([a, b])

q.sort()

hq = []

for i in q:
    if hq and hq[0] <= i[0]:
        heapq.heappushpop(hq, i[1])

    else:
        heapq.heappush(hq, i[1])

print(len(hq))
