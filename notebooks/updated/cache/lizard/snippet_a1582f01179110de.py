def ellipsize(o):
    r = repr(o)
    if len(r) < 800:
        return r
    r = r[:60] + ' ... ' + r[-15:]
    return r