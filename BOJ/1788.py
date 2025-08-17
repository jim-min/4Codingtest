put = int(input())

MOD_BILLION = 1000000000;

fibo = [0, 1]

for i in range(0, 1000000):
    fibo.append((fibo[i] + fibo[i + 1]) % MOD_BILLION)

if (put == 0):
    print(0)
    print(0)

else:
    if (put < 0 and put % 2 == 0):
        print(-1)
    else:
        print(1)
    
    print(fibo[abs(put)])



