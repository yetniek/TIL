
def solution(lottos, win_nums):
    def min_grade(nums, wins):
        tmp = len(list(set(wins) & set(nums)))
        if tmp < 2:
            return 6
        else:
            return (6 - tmp) + 1
    answer = []
    zero = lottos.count(0)
    max_g = (6 - (len(list(set(lottos) & set(win_nums))) + zero)) + 1
    min_g = min_grade(lottos, win_nums)

    if max_g == 7:
        max_g -= 1

    answer.append(max_g)
    answer.append(min_g)

    return answer

def solution2(lottos, win_nums):
    # 맞춘 개수와 0의 개수
    match_count = len(set(lottos) & set(win_nums))
    zero_count = lottos.count(0)

    # 등수 매핑 (0~6 맞춘 개수)
    rank = [6, 6, 5, 4, 3, 2, 1]

    # 최고 등수와 최저 등수 계산
    max_rank = rank[match_count + zero_count]
    min_rank = rank[match_count]

    return [max_rank, min_rank]