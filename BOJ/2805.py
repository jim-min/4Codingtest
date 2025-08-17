import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

lowest, highest = 0, max(trees) - 1

while lowest <= highest:
  mid = (lowest + highest) // 2

  cut = 0

  for i in trees:
    if i > mid:
      cut += i - mid

  if cut >= m:
    lowest = mid + 1

  else:
    highest = mid - 1

print(highest)



