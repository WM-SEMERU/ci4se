def multi_index(idx, dim):

    def _rec(idx, dim):
        idxn = idxm = 0
        if not dim:
            return ()
        if idx == 0:
            return (0,) * dim
        while terms(idxn, dim) <= idx:
            idxn += 1
        idx -= terms(idxn - 1, dim)
        if idx == 0:
            return (idxn,) + (0,) * (dim - 1)
        while terms(idxm, dim - 1) <= idx:
            idxm += 1
        return (int(idxn - idxm),) + _rec(idx, dim - 1)
    return _rec(idx, dim)