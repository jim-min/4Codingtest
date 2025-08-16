import sys

n = int(sys.stdin.readline())
times = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())

    times.append([s, e])

times.sort(key=lambda x:(x[1], x[0]))

ans = 0
start = 0

for i in times:
    if i[0] >= start:
        start = i[1]
        ans += 1

print(ans)
