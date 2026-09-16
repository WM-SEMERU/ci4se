def makerandCIJ_dir(n, k, seed=None):
    rng = get_rng(seed)
    ix, = np.where(np.logical_not(np.eye(n)).flat)
    rp = rng.permutation(np.size(ix))
    CIJ = np.zeros((n, n))
    CIJ.flat[ix[rp][:k]] = 1
    return CIJ