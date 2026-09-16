def point_seg_sep(ar, br1, br2):
    v = br2 - br1
    w = ar - br1
    c1 = np.dot(w, v)
    if c1 <= 0.0:
        return ar - br1
    c2 = np.sum(np.square(v))
    if c2 <= c1:
        return ar - br2
    b = c1 / c2
    bc = br1 + b * v
    return ar - bc