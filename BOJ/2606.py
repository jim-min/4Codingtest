amount_of_pc = int(input())
lines = int(input())

graphs = []

for i in range(lines):
    graphs.append(list(map(int, input().split())))

connected_with = [1]
con_index = 0

while True:
    updated = False

    for i in graphs:
        if connected_with[con_index] in i:
            if i[0] == connected_with[con_index]:
                if i[1] not in connected_with:
                    connected_with.append(i[1])
                    updated = True
            else:
                if i[0] not in connected_with:
                    connected_with.append(i[0])
                    updated = True

    if not updated:
        if con_index == len(connected_with) - 1:
            break

    con_index += 1
    
print(len(connected_with) - 1)
