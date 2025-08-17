# 풀긴 했는데, ai 도움을 받아버림 시작이 잘못돼서
# 다음에 다시 풀기

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    cols = int(sys.stdin.readline())
    
    line_one = list(map(int, sys.stdin.readline().split()))
    line_two = list(map(int, sys.stdin.readline().split()))
    
    li = [[a, b] for a, b in zip(line_one, line_two)]
    best_up = [0] * (cols + 1)   
    best_down = [0] * (cols + 1) 
    
    best_up[1] = li[0][0]
    best_down[1] = li[0][1]
    
    for i in range(2, cols + 1):
        best_up[i] = max(best_down[i-1] + li[i-1][0], 
                        max(best_up[i-2], best_down[i-2]) + li[i-1][0])
        
        best_down[i] = max(best_up[i-1] + li[i-1][1], 
                          max(best_up[i-2], best_down[i-2]) + li[i-1][1])
    
    print(max(best_up[cols], best_down[cols]))

