def RRlist2bitmap(lst):
    import math
    bitmap = b''
    lst = [abs(x) for x in sorted(set(lst)) if x <= 65535]
    max_window_blocks = int(math.ceil(lst[-1] / 256.0))
    min_window_blocks = int(math.floor(lst[0] / 256.0))
    if min_window_blocks == max_window_blocks:
        max_window_blocks += 1
    for wb in range(min_window_blocks, max_window_blocks + 1):
        rrlist = sorted(x for x in lst if 256 * wb <= x < 256 * (wb + 1))
        if not rrlist:
            continue
        if rrlist[-1] == 0:
            bytes_count = 1
        else:
            max = rrlist[-1] - 256 * wb
            bytes_count = int(math.ceil(max // 8)) + 1
        if bytes_count > 32:
            bytes_count = 32
        bitmap += struct.pack('BB', wb, bytes_count)
        bitmap += b''.join(struct.pack(b'B', sum(2 ** (7 - (x - 256 * wb) +
            tmp * 8) for x in rrlist if 256 * wb + 8 * tmp <= x < 256 * wb +
            8 * tmp + 8)) for tmp in range(bytes_count))
    return bitmap