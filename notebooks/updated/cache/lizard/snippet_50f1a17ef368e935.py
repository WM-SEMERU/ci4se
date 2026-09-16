def bootstrapping_count_matrix(Ct, nbs=10000):
    N = Ct.shape[0]
    T = Ct.sum()
    p = Ct.toarray()
    p = np.reshape(p, (N * N,)).astype(np.float)
    p = p / T
    svals = np.zeros((nbs, N))
    for s in range(nbs):
        sel = np.random.multinomial(T, p)
        sC = np.reshape(sel, (N, N))
        svals[(s), :] = scl.svdvals(sC)
    smean = np.mean(svals, axis=0)
    sdev = np.std(svals, axis=0)
    return smean, sdev