n = int(input())

arr = [3, 7, 17, 41]

for i in range(3, n + 1):
    arr.append((arr[i]*2 + arr[i-1])%9901)

print(arr[n-1])

