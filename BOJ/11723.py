import sys

n = int(sys.stdin.readline())
answer_set = set()

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    if command[0] == 'empty':
        answer_set.clear()

    elif command[0] == 'all':
        a = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        answer_set = answer_set.union(a)

    elif command[0] == 'check':
        if int(command[1]) in answer_set:
            print(1)
        
        else:
            print(0)

    elif command[0] == 'toggle':
        if int(command[1]) in answer_set:
            answer_set.remove(int(command[1]))

        else:
            answer_set.add(int(command[1]))

    elif command[0] == 'remove':
        answer_set.discard(int(command[1]))

    elif command[0] == 'add':
        answer_set.add(int(command[1]))
