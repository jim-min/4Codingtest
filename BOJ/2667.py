import sys

def search(u, v):
    global node, graph

    node += 1
    for i in range(4):
        if 0 <= u + dx[i] < n and 0 <= v + dy[i] < n:
            if graph[u + dx[i]][v + dy[i]] == 1:
                graph[u + dx[i]][v + dy[i]] = 0
                search(u + dx[i], v + dy[i])

n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
nodes = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for j in range(n):
    d = sys.stdin.readline().strip()

    for i in range(n):
        graph[j].append(int(d[i]))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            node = 0
            graph[i][j] = 0
            search(i, j)
            
            nodes.append(node)

print(len(nodes))
nodes.sort()
for k in nodes:
    print(k)

