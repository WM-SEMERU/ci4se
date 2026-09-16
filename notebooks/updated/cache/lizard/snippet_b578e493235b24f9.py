def maketoeplitzCIJ(n, k, s, seed=None):
    rng = get_rng(seed)
    from scipy import linalg, stats
    pf = stats.norm.pdf(range(1, n), 0.5, s)
    template = linalg.toeplitz(np.append((0,), pf), r=np.append((0,), pf))
    template *= k / np.sum(template)
    CIJ = np.zeros((n, n))
    itr = 0
    while np.sum(CIJ) != k:
        CIJ = rng.random_sample((n, n)) < template
        itr += 1
        if itr > 10000:
            raise BCTParamError(
                'Infinite loop was caught generating toeplitz matrix.  This means the matrix could not be resolved with the specified parameters.'
                )
    return CIJ