def back(i, lvl):
    if lvl == m:
        print(*ans)

    else:
        if n - i + 1 < m - lvl:
            pass

        else:
            for j in range(i, n + 1):
                ans[lvl] = nums[j - 1]
                back(j + 1, lvl + 1)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [-1] * m
back(1, 0)
