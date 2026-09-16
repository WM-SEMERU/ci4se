def kld(p, q):
    try:
        _check_prob_dist(p)
        _check_prob_dist(q)
    except ValueError:
        return np.nan
    p = p.replace(0, np.nan)
    q = q.replace(0, np.nan)
    return (np.log2(p / q) * p).sum(axis=0)