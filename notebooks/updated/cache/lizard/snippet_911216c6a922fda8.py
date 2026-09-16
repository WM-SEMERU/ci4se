def psturng(q, r, v):
    if all(map(_isfloat, [q, r, v])):
        return _psturng(q, r, v)
    return _vpsturng(q, r, v)