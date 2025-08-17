import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
fail = False
ok = 0
q = []
new = deque()

for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if li[j] == 1:
            new.append([i, j])

    graph.append(li)

q.append(new)

while q:
    level = q.pop()
    new = deque()

    while level:
        one, two = level.popleft()
        for i in range(4):
            oo = one + dx[i]
            tt = two + dy[i]
            if 0 <= oo < n and 0 <= tt < m:
                if graph[oo][tt] == 0:
                    new.append([oo, tt])
                    graph[oo][tt] = 1

    if not new:
        break

    else:
        q.append(new)           

    ok += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            fail = True
            break

if (fail):
    print(-1)

else:
    print(ok)

