def _unify_rows(a):
    lens = np.fromiter(map(len, a), np.int32)
    if not (lens[0] == lens).all():
        out = np.zeros((len(a), lens.max()), np.float32)
        for i, row in enumerate(a):
            out[(i), :lens[i]] = row
    else:
        out = np.float32(a)
    return out