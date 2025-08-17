n, m, k = map(int, input().split())
team = 0
while (n>1 and m>0):
    n -= 2
    m -= 1
    team += 1

while (n>0 and k>0):
    n -= 1
    k -= 1

while (m>0 and k>0):
    m -= 1
    k -= 1

if (k>0):
    print(team - (k+2)//3)

else:
    print(team)



