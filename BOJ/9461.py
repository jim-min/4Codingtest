n = int(input())

arr = [1, 1, 1, 2, 2]

for i in range(4, 101):
    arr.append(arr[i-4] + arr[i])

for _ in range(n):
    k = int(input())
    print(arr[k-1])

