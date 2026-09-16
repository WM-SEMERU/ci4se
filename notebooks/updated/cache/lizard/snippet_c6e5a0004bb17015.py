def union(seq1=(), *seqs):
    r
    if not seqs:
        return list(seq1)
    res = set(seq1)
    for seq in seqs:
        res.update(set(seq))
    return list(res)