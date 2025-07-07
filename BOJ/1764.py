import sys

n, m = map(int, sys.stdin.readline().split())
human = set()
dbz = []

for _ in range(n):
    a = sys.stdin.readline().strip()
    human.add(a)

for _ in range(m):
    b = sys.stdin.readline().strip()
    h_num = len(human)
    human.add(b)
    if (len(human) == h_num):
        dbz.append(b)

print(len(dbz))
dbz.sort()

for i in dbz:
    print(i)
