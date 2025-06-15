n = int(input())

first = input()
second = input()

if first[0] != second[0] or first[-1] != second[-1]:
    print("NO")

else:
    first = first[1:n-1]
    second = second[1:n-1]

    firstDict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    secondDict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    firstCheck = ''
    secondCheck = ''

    for i in first:
        if i in firstDict:
            firstDict[i] += 1

        else:
            firstCheck += i

    for j in second:
        if j in secondDict:
            secondDict[j] += 1

        else:
            secondCheck += j

    if firstCheck != secondCheck or firstDict != secondDict:
        print("NO")

    else:
        print("YES")
