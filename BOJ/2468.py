import sys
sys.setrecursionlimit(10**6)

def dfs(j, k):
    a[j][k] = False
    for i in range(4):
        x = j + dx[i]
        y = k + dy[i]

        if 0 <= x < n and 0 <= y < n:
            if a[x][y]:
                dfs(x, y)

n = int(sys.stdin.readline())
graph = []
m = 0
ans = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    m = max(m, max(li))
    graph.append(li)

for i in range(1, m):
    a = [[True]*n for _ in range(n)]
    zone = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] <= i:
                a[j][k] = False

    for j in range(n):
        for k in range(n):
            if a[j][k]:
                dfs(j, k)
                zone += 1

    ans = max(ans, zone)

print(ans)
