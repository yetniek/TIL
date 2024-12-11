def solution(dartResult):
    answer = 0
    temp = []
    opts = []
    cnt = 0  # 현재 몇 번째 점수인지 추적

    # Step 1: 문자열 파싱
    for i in dartResult:
        if i.isalpha():
            a = dartResult[:((dartResult.index(i)) + 1)]
            temp.append(a)
            dartResult = dartResult.replace(a, '', 1)  # 첫 번째 등장만 제거
            cnt += 1
        elif i in '#*':
            dartResult = dartResult.replace(i, '', 1)  # 첫 번째 등장만 제거
            opts.append((i, cnt - 1))  # 옵션과 대상 점수의 인덱스를 저장

    # Step 2: 점수 계산
    calcul = []
    for value in temp:
        if len(value) > 1:
            nums, bonus = int(value[:-1]), value[-1]
            if bonus == 'S':
                nums = nums ** 1
            elif bonus == 'D':
                nums = nums ** 2
            elif bonus == 'T':
                nums = nums ** 3
            calcul.append(nums)

    # Step 3: 옵션 처리
    for opt, idx in opts:
        if opt == '*':
            calcul[idx] *= 2
            if idx > 0:  # 이전 점수도 2배
                calcul[idx - 1] *= 2
        elif opt == '#':
            calcul[idx] *= -1

    # Step 4: 최종 합산
    answer = sum(calcul)
    return answer


def solution2(dartResult):
    import re

    # Step 1: 정규식으로 점수|보너스|[옵션] 패턴을 추출
    pattern = r"(\d+)([SDT])([*#]?)"
    matches = re.findall(pattern, dartResult)

    # Step 2: 계산 로직 구현
    scores = []
    for i, (num, bonus, option) in enumerate(matches):
        # 점수 계산
        num = int(num)
        if bonus == 'S':
            num **= 1
        elif bonus == 'D':
            num **= 2
        elif bonus == 'T':
            num **= 3

        # 옵션 처리
        if option == '*':
            num *= 2
            if i > 0:  # 이전 점수가 있다면 그것도 2배
                scores[i - 1] *= 2
        elif option == '#':
            num *= -1

        scores.append(num)

    # 총점 계산
    return sum(scores)