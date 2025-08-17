# 방법 1 (dp를 해당 사람들 수를 위해 필요한 가격)

# import sys

# c, n = map(int, sys.stdin.readline().split())
# hotels = {}
# the_cheapest = [999999] * (c + 101)
# the_cheapest[0] = 0

# for _ in range(n):
#     l, m = map(int, sys.stdin.readline().split())

#     if l not in hotels:
#         hotels[l] = m

#     else:
#         if hotels[l] < m:
#             hotels[l] = m
    
# for l, m in hotels.items():
#     for i in range(1, c + 101):
#         if i-m >= 0 and the_cheapest[i] > the_cheapest[i-m] + l:
#             the_cheapest[i] = the_cheapest[i-m] + l

# print(min(the_cheapest[c:]))

# 방법 2 (dp를 특정 가격에 구할 수 있는 최대 인원 수로 구하기)
import sys

c, n = map(int, sys.stdin.readline().split())
hotels = {}
the_cheapest = [0] * (100001)

for _ in range(n):
    l, m = map(int, sys.stdin.readline().split())

    if l not in hotels:
        hotels[l] = m

    else:
        if hotels[l] < m:
            hotels[l] = m

for i in range(1, 100001):
    for j in hotels:
        if the_cheapest[i] < the_cheapest[i-j] + hotels[j] and i-j >= 0:
            the_cheapest[i] = the_cheapest[i-j] + hotels[j]

for i in range(len(the_cheapest)):
    if the_cheapest[i] >= c:
        print(i)
        break

