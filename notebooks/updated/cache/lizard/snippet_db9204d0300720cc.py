def diffvalues(t1, t2, f):
    t1v = set(values(t1, f))
    t2v = set(values(t2, f))
    return t2v - t1v, t1v - t2v