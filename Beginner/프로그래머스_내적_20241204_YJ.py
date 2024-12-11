def solution(a, b):
    answer = 0
    for x, y in zip(a, b):
        temp = x * y
        answer += temp
    return answer