def undo_filter_sub(filter_unit, scanline, previous, result):
    ai = 0
    for i in range(filter_unit, len(result)):
        x = scanline[i]
        a = result[ai]
        result[i] = x + a & 255
        ai += 1