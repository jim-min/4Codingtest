from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
start_x, start_y = 0, 0
graph = []
visited = [[False]*m for _ in range(n)]

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

for i in range(n):
    li = list(map(int, stdin.readline().split()))

    for j in range(m):
        if li[j] == 2:
            start_x, start_y = i, j
            li[j] = 0

    graph.append(li)

q = deque()
q.append([start_x, start_y])

while (q):
    x, y = q.popleft()

    for i in range(4):
        # 이거 x로 써놓긴 했는데, 가로값이 아님... 아무튼 통과는 되는데 x번째 행을 나타내는거라 변수명이 좀 미스
        xx = x + nx[i]
        yy = y + ny[i]
        if 0 <= xx < n and 0 <= yy < m:
            if graph[xx][yy] == 1 and visited[xx][yy] == False:
                q.append([xx, yy])
                graph[xx][yy] = graph[x][y] + 1
                visited[xx][yy] = True

# 이것도 더 나은 방법이 있을 것 같으나 일단은 -1 처리하는 코드
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            graph[i][j] = -1

for i in graph:
    print(*i)

