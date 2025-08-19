a, b, c = map(int, input().split())

n = a*b//c
d = a*b%c / c

if d==0:
    print(n)

else:
    print(str(n) + str(d).strip('0'))
