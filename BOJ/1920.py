# 이건 이분탐색인데 이렇게 풀 필요 없음. 파이썬은 그냥 set 쓰면 더 빠르고 짧음.

n = int(input())

axis = list(map(int, input().split()))
axis.sort()

m = int(input())

x = list(map(int, input().split()))

for i in x:
    start, end = 0, n - 1
    found = 0

    while (start <= end):
        mid = int((start+end)/2)

        if axis[mid] == i:
            found = 1
            break

        elif axis[mid] < i:
            start = mid + 1

        else:
            end = mid - 1

    print(found)
