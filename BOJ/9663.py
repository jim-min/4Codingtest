n = int(input())
total = 0

queenRows = [0] * n

def isPlacable(row, col):
    if col in queenRows[0:row]:
        return False
    
    for i in range(0, row):
        if abs(row - i) == abs(col - queenRows[i]):
            return False
        
    return True

def nqueen(num):
    if num == n:
        global total
        total += 1
        return
    
    for i in range(n):
        queenRows[num] = i
        if not isPlacable(num, i):
            continue
        
        nqueen(num + 1)
        
nqueen(0)
print(total)

