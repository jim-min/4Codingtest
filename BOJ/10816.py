# 실버 4, 해시 맵
# counter 쓰면 더 편함. 근데 코테 볼 때 기억 안 날 거 같아서 안 씀

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
howmanycards = list(map(int, input().split()))
card_dict = dict()

for j in cards:
    if j in card_dict:
        card_dict[j] += 1

    else:
        card_dict[j] = 1

for i in range(m):
    if howmanycards[i] not in card_dict:
        ans = 0

    else:
        ans = card_dict[howmanycards[i]]

    if i == m-1:
        print(ans)

    else:
        print(ans, end=' ')
