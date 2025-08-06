def bt(lvl):
    if lvl == m:
        print(*ans)
        
    else:
        prev = 0
        for j in range(n):
            if not checked[j] and prev != nums[j]:
                ans[lvl] = nums[j]
                prev = nums[j]
                checked[j] = True
                bt(lvl + 1)
                checked[j] = False

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

ans = [0] * m
checked = [False] * n
bt(0)
