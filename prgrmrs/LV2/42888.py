def solution(record):
    answer = []
    uids = {}

    for i in record:
        a = list(i.split())

        if a[0] == "Enter" or a[0] == "Change":
            uids[a[1]] = a[2]

    for i in record:
        a = list(i.split())

        if a[0] == "Enter":
            answer.append(uids[a[1]]+"님이 들어왔습니다.")

        elif a[0] == "Leave":
            answer.append(uids[a[1]]+"님이 나갔습니다.")

    return answer
