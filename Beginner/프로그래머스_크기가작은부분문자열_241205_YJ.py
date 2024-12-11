def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        a = t[i:len(p) + i]

        if int(a) <= int(p):
            answer += 1
        i += 1

    return answer
