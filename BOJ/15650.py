def back(level, now):
    arr[now - 1] = level
    if now == m:
        print(*arr)
    
    else:
        for i in range(level + 1, n + 1):
            back(i, now + 1)

n, m = map(int, input().split())

for i in range(1, n + 2 - m):
    arr = [i] * m
    back(i, 1)



