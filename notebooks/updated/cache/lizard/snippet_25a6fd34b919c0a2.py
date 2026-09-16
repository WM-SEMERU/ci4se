def min_max_indexes(seq):
    l = sorted(enumerate(seq), key=lambda s: s[1])
    return l[0][0], l[-1][0]