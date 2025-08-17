n, m = map(int, input().split())

d = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

for i in range(1, n + 1):
    t = str(i)

    for j in t:
        d[int(j)] += 1

print(d[m])

