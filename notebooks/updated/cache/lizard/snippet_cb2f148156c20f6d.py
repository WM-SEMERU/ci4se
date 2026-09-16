def masked(a, b):
    if np.any([a.dtype.kind.startswith(c) for c in ['i', 'u', 'f', 'c']]):
        n = np.array([np.nan for i in range(len(a))])
    else:
        n = np.array([None for i in range(len(a))])
    return np.where(b, a, n)