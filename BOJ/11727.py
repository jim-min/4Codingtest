n = int(input())

method = [0, 1, 3]

for i in range(3, 1001):
    method.append(method[i-1] + 2*method[i-2])

print(method[n] % 10007)
