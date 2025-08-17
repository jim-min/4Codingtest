n = int(input())
rgbs = []

for _ in range(n):
    rgb = list(map(int, input().split()))
    rgbs.append(rgb)
    
ans = [[0, 0, 0] for _ in range(n + 2)]

for idx, _ in enumerate(rgbs):
    ans[idx + 1][0] = min(ans[idx][1], ans[idx][2]) + rgbs[idx][0]
    ans[idx + 1][1] = min(ans[idx][0], ans[idx][2]) + rgbs[idx][1]
    ans[idx + 1][2] = min(ans[idx][1], ans[idx][0]) + rgbs[idx][2]

print(min(ans[n][0], ans[n][1], ans[n][2]))

