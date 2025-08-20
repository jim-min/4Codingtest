n = list(input().strip())
bomb = list(input().strip())
lb = len(bomb)

# 시간 초과된 풀이
# done = False

# while (not done):
#     done = True

#     for i in range(len(n)):
#         if n[i:i+lb] == bomb:
#             n = n[:i] + n[i+lb:]
#             done = False

stack = []

for i in n:
    stack.append(i)
    if (stack[-lb:] == bomb):
        for _ in range(lb):
            stack.pop()

if not stack:
    print("FRULA")

else:
    print(*stack, sep='')
