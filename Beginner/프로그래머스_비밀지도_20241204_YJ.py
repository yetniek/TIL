def solution(n, arr1, arr2):
    maps = []
    answer = []

    def add_map(arr):
        arrs = []
        for i in arr:
            tmp = ''
            while i != 0:
                num = i % 2
                if num == 0:
                    tmp += '0'
                else:
                    tmp += '1'
                i //= 2

            tmp = tmp[::-1]
            if len(tmp) != n:
                tmp = '0' * (n - len(tmp)) + tmp
            arrs.append(tmp)
        return arrs

    map1 = add_map(arr1)
    map2 = add_map(arr2)

    for m1, m2 in zip(map1, map2):
        tmps = ''
        for i, j in zip(m1, m2):
            i, j = int(i), int(j)
            tmp = i + j
            if tmp == 2:
                tmp = 1
            tmps += str(tmp)
        maps.append(tmps)

    for map in maps:
        map = map.replace('1', '#')
        map = map.replace('0', ' ')
        answer.append(map)

    return answer