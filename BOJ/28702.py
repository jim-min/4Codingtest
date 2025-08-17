def fb(n):
    if n%5 == 0:
        if n%3 == 0:
            print("FizzBuzz")

        else:
            print("Buzz")

    else:
        if n%3 == 0:
            print("Fizz")

        else:
            print(n)

def int_or_not(a,b,c):
    if a.upper() == a:
        a = int(a)
        return a, 3

    elif b.upper() == b:
        b = int(b)
        return b, 2
    
    else:
        c = int(c)
        return c, 1


a = input()
b = input()
c = input()

m, n = int_or_not(a,b,c)

fb(m+n)



