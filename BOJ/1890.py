import sys

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    li = list(map(int, sys.stdin.readline().split()))
    graph.append(li)

jumpable = [[0]*n for _ in range(n)]
jumpable[0][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] >= 1:
            jump = graph[i][j]
            if i + jump <= n - 1:
                jumpable[i+jump][j] += jumpable[i][j]

            if j + jump <= n - 1:
                jumpable[i][j+jump] += jumpable[i][j]

print(jumpable[n-1][n-1])