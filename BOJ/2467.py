# 골드 5, 이분 탐색; 투 포인터로 하면 더 빨리 풀 수 있음

n = int(input())

liquid = list(map(int, input().split()))

a, b = liquid[0], liquid[1]
least = abs(a + b)

while (len(liquid) > 1):
    first = liquid.pop(0)

    start = 0
    end = len(liquid) - 1

    while (start <= end):
        mid = (start + end) // 2

        if liquid[mid] >= -first:
            end = mid - 1

        else:
            start = mid + 1

        if (abs(first + liquid[mid]) < least):
            least = abs(first + liquid[mid])
            a, b = first, liquid[mid]

print(a, b)
