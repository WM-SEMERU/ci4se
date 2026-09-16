def single_index(idxm):
    if -1 in idxm:
        return 0
    order = int(sum(idxm))
    dim = len(idxm)
    if order == 0:
        return 0
    return terms(order - 1, dim) + single_index(idxm[1:])