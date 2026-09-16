def _hkt(eivals, timescales, normalization, normalized_laplacian):
    nv = eivals.shape[0]
    hkt = np.zeros(timescales.shape)
    for idx, t in enumerate(timescales):
        hkt[idx] = np.sum(np.exp(-t * eivals))
    if isinstance(normalization, np.ndarray):
        return hkt / normalization
    if normalization == 'empty' or normalization == True:
        return hkt / nv
    if normalization == 'complete':
        if normalized_laplacian:
            return hkt / (1 + (nv - 1) * np.exp(-timescales))
        else:
            return hkt / (1 + nv * np.exp(-nv * timescales))
    return hkt