def weir_cockerham_fst(g, subpops, max_allele=None, blen=None):
    if not hasattr(g, 'shape') or not hasattr(g, 'ndim'):
        g = GenotypeArray(g, copy=False)
    if g.ndim != 3:
        raise ValueError('g must have three dimensions')
    if g.shape[2] != 2:
        raise NotImplementedError('only diploid genotypes are supported')
    if max_allele is None:
        max_allele = g.max()
    blen = get_blen_array(g, blen)
    n_variants = g.shape[0]
    shape = n_variants, max_allele + 1
    a = np.zeros(shape, dtype='f8')
    b = np.zeros(shape, dtype='f8')
    c = np.zeros(shape, dtype='f8')
    for i in range(0, n_variants, blen):
        j = min(n_variants, i + blen)
        gb = g[i:j]
        ab, bb, cb = _weir_cockerham_fst(gb, subpops, max_allele)
        a[i:j] = ab
        b[i:j] = bb
        c[i:j] = cb
    return a, b, c