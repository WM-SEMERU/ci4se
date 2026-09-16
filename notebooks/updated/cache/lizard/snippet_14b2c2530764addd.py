def scalogram(M, circ=False):
    if not type(M) is np.ndarray:
        M = np.array(M)
    if M.shape[0] != M.shape[1]:
        raise ValueError('Matrix is not square.')
    try:
        n = min(M.shape)
    except AttributeError:
        n = M.size
    N = np.zeros(M.shape)
    for i in range(n):
        for j in range(n):
            if i + j < n and i >= j:
                N[i, j] = M[(i), i - j:i + j + 1].sum()
            elif circ and i + j < n and i < j:
                N[i, j] = M[(i), i - j:].sum() + M[(i), :i + j + 1].sum()
            elif circ and i >= j and i + j >= n:
                N[i, j] = M[(i), i - j:].sum() + M[(i), :i + j - n + 1].sum()
            elif circ and i < j and i + j >= n:
                N[i, j] = M[(i), i - j:].sum() + M[(i), :].sum() + M[(i), :
                    i + j - n + 1].sum()
    return N