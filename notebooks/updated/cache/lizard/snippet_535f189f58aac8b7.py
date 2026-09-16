def segment_area(seg):
    r0 = seg[0][COLS.R]
    r1 = seg[1][COLS.R]
    h2 = point_dist2(seg[0], seg[1])
    return math.pi * (r0 + r1) * math.sqrt((r0 - r1) ** 2 + h2)