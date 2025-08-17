ppl = int(input())
ppls=[]
scrs=[]

for i in range(ppl):
    conNum, conPpl, scr= map(int, input().split())
    scrs.append([scr, i])
    ppls.append([conNum, conPpl])
    
scrs.sort(reverse=True)

checCon=ppls[scrs[0][1]][0]
cnt=2

print(ppls[scrs[0][0]][0], ppls[scrs[0][1]][1])
print(ppls[scrs[1][0]][0], ppls[scrs[1][1]][1])

if checCon==ppls[scrs[1]][0]:
    while checCon==ppls[scrs[cnt]][0]:
        cnt+=1
        
print(ppls[scrs[cnt][0]][0], ppls[scrs[cnt][1][1]])

