def dfs(depth):
    if depth==m:
        print(' '.join(map(str, result)))
        
    for i in range(n):
        if not vist[i]:
            result.append(numList[i])
            vist[i] = True
            dfs(depth + 1)
            result.pop()
            vist[i] = False

n, m = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort()

vist=[False]*n
result = []

dfs(0)