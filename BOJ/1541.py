# 솔직히 정규표현식은 내가 짤 자신이 없다

import re

stmt = list(input().strip())

minus = False

for i in range(len(stmt)):
    if not minus:
        if stmt[i] == '-':
            minus = True
    
    else:
        if stmt[i] == '+':
            stmt[i] = '-'

stmt = ''.join(stmt)

tokens = re.findall(r'\d+|\D', stmt)
for i in range(len(tokens)):
    if tokens[i].isdigit():
        tokens[i] = str(int(tokens[i])) 

stmt = ''.join(tokens)

print(eval(stmt))

