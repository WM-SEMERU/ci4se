def combine_HSPs(a):
    m = a[0]
    if len(a) == 1:
        return m
    for b in a[1:]:
        assert m.query == b.query
        assert m.subject == b.subject
        m.hitlen += b.hitlen
        m.nmismatch += b.nmismatch
        m.ngaps += b.ngaps
        m.qstart = min(m.qstart, b.qstart)
        m.qstop = max(m.qstop, b.qstop)
        m.sstart = min(m.sstart, b.sstart)
        m.sstop = max(m.sstop, b.sstop)
        if m.has_score:
            m.score += b.score
    m.pctid = 100 - (m.nmismatch + m.ngaps) * 100.0 / m.hitlen
    return m