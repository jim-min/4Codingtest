# https://level.goorm.io/exam/355184/%EC%82%BC%EA%B0%81%ED%98%95-%EC%A0%91%EA%B8%B0/quiz/1
# 삼각형 접기 / 최대공약수 구하기

def Euclidean(a, b):
    while b != 0:
        a, b = b, a%b
    return a

b, c = map(int, input().split())
n = Euclidean(b, c)

print(str(b//n)+':'+str(c//n))
