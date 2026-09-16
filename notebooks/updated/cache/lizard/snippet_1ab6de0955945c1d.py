def colwise_diag_idxs(size, num=2):
    r
    import utool as ut
    diag_idxs = ut.iprod(*[range(size) for _ in range(num)])
    upper_diag_idxs = [tup[::-1] for tup in diag_idxs if all([(a > b) for a,
        b in ut.itertwo(tup)])]
    return upper_diag_idxs