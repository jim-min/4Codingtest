import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    li = list(map(int, sys.stdin.readline().split()))

    for j in range(1, n):
            li[j] = li[j - 1] + li[j]

    if i == 0:
        pass

    else:
        for j in range(n):
            li[j] = li[j] + graph[i - 1][j]

    graph.append(li)

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    if x1 == 1 and y1 == 1:
        ans = graph[x2 - 1][y2 - 1]

    elif x1 == 1:
        ans = graph[x2 - 1][y2 - 1] - graph[x2 - 1][y1 - 2]

    elif y1 == 1:
        ans = graph[x2 - 1][y2 - 1] - graph[x1 - 2][y2 - 1]

    else:
        ans = graph[x2 - 1][y2 - 1] - graph[x1 - 2][y2 - 1] - graph[x2 - 1][y1 - 2] + graph[x1 - 2][y1 - 2]

    print(ans)
