def aveknt(t, k):
    t = np.atleast_1d(t)
    if t.ndim > 1:
        raise ValueError('t must be a list or a rank-1 array')
    n = t.shape[0]
    u = max(0, n - (k - 1))
    out = np.empty((u,), dtype=t.dtype)
    for j in range(u):
        out[j] = sum(t[j:j + k]) / k
    return out