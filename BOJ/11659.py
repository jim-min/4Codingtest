import sys # stdin.readline 안 쓰면 시간 초과남 - PyPy는 되긴 함

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
accumulated_sum = [0] * (n + 1)
accumulated_sum[1] = nums[0]
idx = 0

for i in nums:
    if idx == 0:
        idx += 1
        continue

    accumulated_sum[idx + 1] = accumulated_sum[idx] + i
    idx += 1


for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(accumulated_sum[j] - accumulated_sum[i - 1])

