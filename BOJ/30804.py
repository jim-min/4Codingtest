n = int(input())

th = list(map(int, input().split()))
th_dict = {}
left = 0
maxsize = 0

for i in range(n):
    if len(th_dict) < 2 and th[i] not in th_dict:
        th_dict[th[i]] = 1

    elif th[i] not in th_dict:
        th_dict[th[i]] = 1

        while (len(th_dict) > 2):
            th_dict[th[left]] -= 1
            if th_dict[th[left]] == 0:
                del th_dict[th[left]]

            left += 1

    elif th[i] in th_dict:
        th_dict[th[i]] += 1
        
    if (maxsize < i - left + 1):
        maxsize = i - left + 1

print(maxsize)

