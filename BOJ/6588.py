import sys

lim = 1000000
c = [False, False] + [True] * (lim - 1)
primes = []

for i in range(2, lim//2 + 1):
    if c[i] == False:
        continue

    primes.append(i)

    for j in range(2*i, lim + 1, i):
        c[j] = False

n = int(sys.stdin.readline())

while (n != 0):
    if (n % 2 == 1):
        print("Goldbach's conjecture is wrong.")
        n = int(sys.stdin.readline())
        continue
        
    for k in primes:
        first = k
        second = n - first

        if c[second]:
            print(n, "=", first, "+", second)
            break

    n = int(sys.stdin.readline())

