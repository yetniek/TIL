def solution(numbers):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    temp = set(check) - set(numbers)

    return sum(temp)