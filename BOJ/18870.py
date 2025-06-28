# 이 풀이 말고 set, dictionary 쓰는 해법이 더 빠르다

n = int(input())

li = list(map(int, input().split()))
idx_li = []

for i in range(n):
    idx_li.append([li[i], i])

idx_li.sort()

start = -1
key = -1000000001

for j in idx_li:
    if key != j[0]:
        start += 1

    key = j[0]
    j[0] = start

idx_li.sort(key=lambda x:x[1])

for k in idx_li:
    if k == idx_li[-1]:
        print(k[0])
    else:
        print(k[0], end=" ")
