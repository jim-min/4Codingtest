import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    global visited, lines, howmany
    visited[v] = True

    for k in graph[v]:
        if not visited[k]:
            if lines[k] == "P":
                howmany += 1
            dfs(k)

n, m = map(int, input().split())
i = 0
howmany = 0

graph = [[] for _ in range(n*m + 1)]
visited = [False] * (n*m + 1)

lines = "."

for i in range(n):
    lines += input()

idx = 1
while (idx < n*m):
    if lines[idx] == "X":
        idx += 1
        continue

    if lines[idx] == "I":
        i = idx

    if idx % m != 0:
        if lines[idx + 1] == "O" or lines[idx + 1] == "P":
            graph[idx].append(idx + 1)
            graph[idx + 1].append(idx)

    if idx >= n*m - m:
        idx += 1
        continue

    if lines[idx + m] == "O" or lines[idx + m] == "P":
        graph[idx].append(idx + m)
        graph[idx + m].append(idx)

    idx += 1

dfs(i)

if howmany:
    print(howmany)

else:
    print("TT")
