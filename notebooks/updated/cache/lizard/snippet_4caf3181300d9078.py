def meta(r):
    r = r.split()
    assert len(r) == 5
    r = [r[0]] + map(int, r[1:])
    return r