# 풀이 1, DFS로 풀었을 때

# import sys
# sys.setrecursionlimit(10**6)

# a, b = map(int, input().split())
# ans = 999999

# def gogo(i, rec):
#     global ans
    
#     if i == b:
#         if ans > rec:
#             ans = rec

#     elif i > b:
#         return

#     else:
#         gogo(i*2, rec + 1)
#         gogo(i*10+1, rec + 1)

# gogo(a, 1)

# if ans == 999999:
#     ans = -1

# print(ans)

# 풀이 2, BFS 정석 풀이 (왜 백준상에선 더 오래 걸리지)

from collections import deque

a, b = map(int, input().split())
printed = False

q = deque()
q.append([a,1])

while (q):
    s, rec = q.popleft()
    if s == b:
        print(rec)
        printed = True
        break

    if (s*2 <= b):
        q.append([s*2, rec + 1])

    if (s*10 + 1 <= b):
        q.append([s*10 + 1, rec + 1])

if not printed:
    print(-1)
