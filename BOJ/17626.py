# PyPy 필요, DP

import math

n = int(input())

arr = [0, 1]

for i in range(2, n + 1):
    mint = 5
    for j in range(1, int(math.sqrt(i)) + 1):
        mint = min(mint, arr[i - j**2])

    arr.append(mint + 1)
    
print(arr[n])


