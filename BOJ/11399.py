ppl = int(input())

costs = list(map(int, input().split()))
costs.sort()

ans = 0

for idx, _ in enumerate(costs):
    for j in range(idx + 1):
        ans += costs[j]

print(ans)



