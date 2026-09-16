def find_all(s, sub, start=0, end=0, limit=-1, reverse=False):
    indexes = []
    if not bool(s and sub):
        return indexes
    lstr = len(s)
    if lstr <= start:
        return indexes
    lsub = len(sub)
    if lstr < lsub:
        return indexes
    if limit == 0:
        return indexes
    elif limit < 0:
        limit = lstr
    end = min(end, lstr) or lstr
    idx = s.rfind(sub, start, end) if reverse else s.find(sub, start, end)
    while idx != -1:
        indexes.append(idx)
        if reverse:
            idx = s.rfind(sub, start, idx - lstr)
        else:
            idx = s.find(sub, idx + lsub, end)
        if len(indexes) >= limit:
            break
    return indexes