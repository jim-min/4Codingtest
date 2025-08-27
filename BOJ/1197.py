import sys
sys.setrecursionlimit(10**8)

def find(i):
    if connected[i] == i:
        return i
    
    connected[i] = find(connected[i]) # 이후의 recursion 줄이기 위해 경로 압축 
    return connected[i]

def union(i, j):
    a = find(i)
    b = find(j)

    # 이렇게 하면 경로가 깔끔해지긴 하는데 그냥 어디에 붙여도 작동하는 데에 상관은 없는 듯
    if a > b:
        connected[a] = b

    else:
        connected[b] = a

v, e = map(int, sys.stdin.readline().split())

graph = []
connected = list(range(v))
ans = 0
edges = 0

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())

    # 인덱스 0부터 시작할 수 있게 노드 번호에 1씩 빼줌, sort 편하게 가중치 0번에 둠
    graph.append((c, a - 1, b - 1))

graph.sort()

for weight, a, b in graph:
    if find(a) != find(b):
        union(a, b)

        ans += weight
        edges += 1

    if edges == v - 1:
        break

print(ans)
