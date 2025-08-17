from math import ceil

n = int(input())

shirts = list(map(int, input().split()))
t, p = map(int, input().split())

result = 0

for i in shirts:
    result += ceil(i/t)

print(result)

print(n//p, n%p)

