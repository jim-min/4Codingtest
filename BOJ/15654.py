# def dfs(depth):
#     if depth==m:
#         print(' '.join(map(str, result)))
        
#     for i in range(n):
#         if not vist[i]:
#             result.append(numList[i])
#             vist[i] = True
#             dfs(depth + 1)
#             result.pop()
#             vist[i] = False

# n, m = map(int, input().split())
# numList = list(map(int, input().split()))

# numList.sort()

# vist=[False]*n
# result = []

# dfs(0)

# 이걸 내가 언제 풀었는지 모르겠음

def solve(i, lvl):
    global ans

    if (lvl == m):
        print(*ans)

    else:
        for j in range(n):
            if nums[j] not in ans[0:lvl]:
                ans[lvl] = nums[j]
                solve(j + 1, lvl + 1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [-1] * m
solve(0, 0)
