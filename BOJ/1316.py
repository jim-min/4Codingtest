amount = int(input())
answer = 0

for i in range(amount):
    word_checker = input()
    word = ''
    words = []
    word_wrong = False
    
    for j in word_checker:
        if j == word:
            continue
        
        words.append(j)
        word = j
        if words.count(j) > 1:
            word_wrong = True
            
    if not word_wrong:
        answer += 1
        
print(answer)