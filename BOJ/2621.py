a, one = input().strip().split()
b, two = input().strip().split()
c, three = input().strip().split()
d, four = input().strip().split()
e, five = input().strip().split()

colors = [a, b, c, d, e]
nums = sorted(list(map(int, [one, two, three, four, five])))
score = max(nums)

is_straight = False
checks = list(range(1, 10))

for i in range(5):
    if checks[i:i+5] == nums:
        is_straight = True

is_flush = len(set(colors)) == 1

if is_straight:
    if is_flush:
        # 스티플 
        print(900 + score)

    else:
        # 스트레이트
        print(500 + score)

else:
    if len(set(nums)) == 2:
        same_num = 1
        first = min(nums)

        for i in nums[1:5]:
            if i == first:
                same_num += 1

        # 포카드
        if same_num == 4:
            print(800 + first)

        elif same_num == 1:
            print(800 + nums[-1])

        else:
            # 풀하우스
            if same_num == 2:
                print(700 + nums[-1]*10 + first)

            else:
                print(700 + first*10 + nums[-1])

    elif is_flush:
        # 플러시
        print(600 + score)

    elif len(set(nums)) == 5:
        # 꽝
        print(100 + score)

    else:
        dic = {}
        pairs = 0
        paired = []

        for i in nums:
            if i not in dic:
                dic[i] = 1

            else:
                dic[i] += 1

        for j in dic:
            if dic[j] == 3:
                # 3카드
                print(400 + j)

            elif dic[j] == 2:
                pairs += 1
                paired.append(j)

        if pairs == 1:
            # 1페어
            print(200 + paired[0])

        if pairs == 2:
            # 2페어
            print(300 + paired[1] *10 + paired[0])
