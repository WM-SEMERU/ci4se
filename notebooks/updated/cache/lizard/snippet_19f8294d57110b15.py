def guess_rank(M_E):
    n, m = M_E.shape
    epsilon = np.count_nonzero(M_E) / np.sqrt(m * n)
    _, S0, _ = svds_descending(M_E, min(100, max(M_E.shape) - 1))
    S0 = np.diag(S0)
    S1 = S0[:-1] - S0[1:]
    S1_ = S1 / np.mean(S1[-10:])
    r1 = 0
    lam = 0.05
    cost = [None] * len(S1_)
    while r1 <= 0:
        for idx in range(len(S1_)):
            cost[idx] = lam * max(S1_[idx:]) + idx
        i2 = np.argmin(cost)
        r1 = np.max(i2)
        lam += 0.05
    cost = [None] * (len(S0) - 1)
    for idx in range(len(S0) - 1):
        cost[idx] = (S0[idx + 1] + np.sqrt(idx * epsilon) * S0[0] / epsilon
            ) / S0[idx]
    i2 = np.argmin(cost)
    r2 = np.max(i2 + 1)
    r = max([r1, r2])
    return r