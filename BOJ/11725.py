import sys
sys.setrecursionlimit(10**6)

def dfs(u):
    global parent_nodes, visited, tree

    for i in tree[u]:
        if not visited[i]:
            parent_nodes[i] = u
            visited[i] = True
            dfs(i)

n = int(sys.stdin.readline())

tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent_nodes = [-1] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)

dfs(1)

for j in range(2, n + 1):
    print(parent_nodes[j])

