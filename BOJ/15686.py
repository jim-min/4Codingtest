from itertools import combinations

n, m = map(int, input().split())
homes = []
chicken = []
c_dist = []
ans = 999999999

# 집 / 치킨집 분류
for i in range(n):
    a = list(map(int, input().split()))

    for j in range(n):
        if a[j] == 1:
            homes.append([i, j])

        elif a[j] == 2:
            chicken.append([i, j])

# 모든 치킨집에 대해 치킨 거리 구하기
for home in homes:
    li = []

    for ck in chicken:
        dist = abs(home[0] - ck[0]) + abs(home[1] - ck[1])

        li.append(dist)

    c_dist.append(li)

# 어떤 치킨집을 골라야 치킨거리가 최소일까 판단
com = list(range(len(chicken)))

for k in combinations(com, m):
    least = 0
    
    for i in c_dist:
        dist = []
        for j in k:
            dist.append(i[j])
        least += min(dist)
    
    if least < ans:
        ans = least

print(ans)
