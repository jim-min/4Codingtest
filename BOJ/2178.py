import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[-1]*m for _ in range(n)]
nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

for i in range(n):
    g = sys.stdin.readline().strip()

    for j in range(m):
        graph[i][j] = int(g[j])

q = deque()
q.append([0, 0])

while q:
    x, y = q.popleft()

    for k in range(4):
        xx, yy = x + nx[k], y + ny[k]
        
        if 0 <= xx < n and 0 <= yy < m:
            if graph[xx][yy] == 1:
                q.append([xx, yy])
                graph[xx][yy] = graph[x][y] + 1

print(graph[n-1][m-1])

