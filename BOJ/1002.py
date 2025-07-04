def distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1

    dist_squared = x**2 + y**2
    return dist_squared ** 0.5

n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = distance(x1, y1, x2, y2)

    if (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    
    elif dist > r1 + r2 or dist < abs(r1 - r2):
        print(0)  # 원이 안 닿는 경우

    elif dist == r1 + r2 or dist == abs(r1 - r2):
        print(1)  # 내접까지 고려해줘야 함

    elif dist < r1 + r2:
        print(2)
