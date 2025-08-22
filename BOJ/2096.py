import sys

n = int(sys.stdin.readline())

max_dp = [0,0,0]
small_dp = [0,0,0]

a, b, c = map(int, sys.stdin.readline().split())

max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())

    temp = [0, 0, 0]

    temp[0] = max(max_dp[0], max_dp[1]) + a
    temp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + b
    temp[2] = max(max_dp[1], max_dp[2]) + c

    max_dp = temp

    temp2 = [0, 0, 0]

    temp2[0] = min(min_dp[0], min_dp[1]) + a
    temp2[1] = min(min_dp[0], min_dp[1], min_dp[2]) + b
    temp2[2] = min(min_dp[1], min_dp[2]) + c

    min_dp = temp2

print(max(max_dp), end=' ')

print(min(min_dp))
