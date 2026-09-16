def _noise(seq, c, size=33, total=1000):
    reads = dict()
    seen = 0
    while seen < total:
        s = random.randint(0, len(seq) - size)
        e = s + size + random.randint(-5, 5)
        p = random.uniform(0, 0.1)
        counts = int(p * total) + 1
        seen += counts
        name = 'seq_%s_%s_%s_x%s' % (c, s, e, counts)
        reads[name] = seq[s:e], counts
    return reads