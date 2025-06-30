k, n = map(int, input().split())

lan_cables = []

for _ in range(k):
    a = int(input())
    
    lan_cables.append(a)

start = 1
longest = max(lan_cables)

answer = 0

while (start <= longest):
    mid = (start + longest) // 2

    lans = 0

    for i in lan_cables:
        m = i // mid

        lans += m

    if (lans >= n):
        if (answer < mid):
            answer = mid
        
        start = mid + 1

    else:
        longest = mid - 1

print(answer)
