def _expand(dat, counts, start, end):
    for pos in range(start, end):
        for s in counts:
            dat[s][pos] += counts[s]
    return dat