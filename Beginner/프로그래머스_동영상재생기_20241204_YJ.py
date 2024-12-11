def solution(video_len, pos, op_start, op_end, commands):
    def time_to_sec(time):
        m, s = time.split(":")
        return (int(m) * 60) + int(s)

    def sec_to_time(sec):
        m, s = divmod(sec, 60)
        return str(m).zfill(2) + ":" + str(s).zfill(2)

    answer = ''

    video_len_sec = time_to_sec(video_len)
    pos_sec = time_to_sec(pos)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)

    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    for c in commands:
        if c == 'prev':
            pos_sec = max(0, pos_sec - 10)
        elif c == 'next':
            pos_sec = min(video_len_sec, pos_sec + 10)

        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    answer = sec_to_time(pos_sec)
    return answer