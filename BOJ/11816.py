n = input().strip()
base16 = { 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15 }

if n[1] == 'x':
    n = n[2:]
    s = 0
    k = len(n) - 1
    for i in n:
        if i.isdigit():
            j = int(i)

        else:
            j = base16[i]
        
        s += 16**k * j
        k -= 1

    print(s)

elif n[0] == '0':
    n = n[1:]
    s = 0
    k = len(n) - 1

    for i in n:
        s += 8**k * int(i)
        k -= 1

    print(s)

else:
    print(int(n))

