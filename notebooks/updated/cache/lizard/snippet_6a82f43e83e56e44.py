def find_complement(am, sites=None, bonds=None, asmask=False):
    r
    if sites is not None and bonds is None:
        inds = sp.unique(sites)
        N = am.shape[0]
    elif bonds is not None and sites is None:
        inds = sp.unique(bonds)
        N = int(am.nnz / 2)
    elif bonds is not None and sites is not None:
        raise Exception('Only one of sites or bonds can be specified')
    else:
        raise Exception('Either sites or bonds must be specified')
    mask = sp.ones(shape=N, dtype=bool)
    mask[inds] = False
    if asmask:
        return mask
    else:
        return sp.arange(N)[mask]