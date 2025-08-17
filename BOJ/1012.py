import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    global graph

    for i in range(4):
        nh = x + dh[i]
        nw = y + dw[i]

        if (0 <= nh < m) and (0 <= nw < n):
            if graph[nh][nw] == 1:
                graph[nh][nw] = 0
                dfs(nh, nw)

tc = int(input())
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

for _ in range(tc):
    ans = 0
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())

        graph[x][y] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)
