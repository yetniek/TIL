from itertools import permutations
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    tmp = set()  # 중복 제거

    # 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for p in perms:
            num = int(''.join(p))  # 순열을 숫자로 변환
            tmp.add(num)  # 집합에 추가 (중복 제거)

    # 소수 판별
    for num in tmp:
        if is_prime(num):
            # print(num)  # 소수 출력
            answer += 1

    return answer