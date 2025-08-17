care_time = int(input())
candy_amount = int(input())
candyz = list(map(int, input().split()))

if sum(candyz) >= care_time :
    print("Padaeng_i Happy")
    
else:
    print("Padaeng_i Cry")



