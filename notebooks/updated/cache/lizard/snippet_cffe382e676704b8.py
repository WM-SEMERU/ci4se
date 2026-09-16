def threshold_proportional(W, p, copy=True):
    from .miscellaneous_utilities import teachers_round as round
    if p > 1 or p < 0:
        raise BCTParamError('Threshold must be in range [0,1]')
    if copy:
        W = W.copy()
    n = len(W)
    np.fill_diagonal(W, 0)
    if np.allclose(W, W.T):
        W[np.tril_indices(n)] = 0
        ud = 2
    else:
        ud = 1
    ind = np.where(W)
    I = np.argsort(W[ind])[::-1]
    en = int(round((n * n - n) * p / ud))
    W[ind[0][I][en:], ind[1][I][en:]] = 0
    if ud == 2:
        W[:, :] = W + W.T
    return W