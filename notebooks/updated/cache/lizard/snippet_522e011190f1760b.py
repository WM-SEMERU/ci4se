def ranges_intersect(rset):
    if not rset:
        return None
    a = rset[0]
    for b in rset[1:]:
        if not a:
            return None
        a = range_intersect(a, b)
    return a