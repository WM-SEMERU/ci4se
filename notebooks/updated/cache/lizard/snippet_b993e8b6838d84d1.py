def _sample_without_replacement(n, r, out):
    k = r.shape[0]
    pool = np.arange(n)
    for j in range(k):
        idx = int(np.floor(r[j] * (n - j)))
        out[j] = pool[idx]
        pool[idx] = pool[n - j - 1]