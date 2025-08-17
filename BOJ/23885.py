n, m = map(int, input().split())

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())


if (a1 == b1 and a2 == b2):
    print("YES")

elif (n == 1 or m == 1):
        print("NO")

else: 
    if ((a1+a2) % 2 != (b1+b2) % 2): # (a1+a2)를 괄호로 안 감싸고 %2 해서 자꾸 틀렸음...
        print("NO")
    
    else:
        print("YES")

