def match_window(in_data, offset):
    window_start = max(offset - WINDOW_MASK, 0)
    for n in range(MAX_LEN, THRESHOLD - 1, -1):
        window_end = min(offset + n, len(in_data))
        if window_end - offset < THRESHOLD:
            return None
        str_to_find = in_data[offset:window_end]
        idx = in_data.rfind(str_to_find, window_start, window_end - n)
        if idx != -1:
            code_offset = offset - idx
            code_len = len(str_to_find)
            return code_offset, code_len
    return None