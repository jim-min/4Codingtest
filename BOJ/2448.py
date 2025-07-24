n = int(input())
first = 3
until = first
ans = [""] * n

ans[0] = "  *  "
ans[1] = " * * "
ans[2] = "*****"

while (n != first):
    t = first
    for j in range(first, first * 2):
        ans[j] = ans[j - first] + ' ' * (2*(((t + 2) // 3 - 1) * 3) + 1) + ans[j - first]
        t -= 1

    first = first * 2

for i in ans:
    ws = ((n + 2) // 3 - 1) * 3
    i = ' ' * ws + i + ' ' * ws
    print(i)

    n -= 1
