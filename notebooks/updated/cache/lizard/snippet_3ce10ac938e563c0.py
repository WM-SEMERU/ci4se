def zip_fit_params(data):
    genes, cells = data.shape
    m = data.mean(1)
    v = data.var(1)
    M = (v - m) / (m ** 2 + v - m)
    M = np.array([min(1.0, max(0.0, x)) for x in M])
    L = m + v / m - 1.0
    L[np.isnan(L)] = 0.0
    L = np.array([max(0.0, x) for x in L])
    return L, M