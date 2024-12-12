def get_len_divisor(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)
    return len(divisorsList)


def solution(number, limit, power):
    answer = 0
    counts = []

    for i in range(1, number + 1):
        counts.append(get_len_divisor(i))

    for i, c in enumerate(counts):
        if c > limit:
            counts[i] = power
        else:
            pass

    return sum(counts)