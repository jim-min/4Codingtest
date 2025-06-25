n, m = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(m):
    i, j = map(int, input().split())

    print(sum(nums[i-1:j]))
