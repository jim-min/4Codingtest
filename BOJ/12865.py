import sys

n, k = map(int, sys.stdin.readline().split())
items = []

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())

    items.append([w, v])

dp = [0] * (k + 1)

for w, v in items:
    for i in range(k, w-1, -1):
        if dp[i] < dp[i-w] + v:
            dp[i] = dp[i-w] + v

print(dp[k])
