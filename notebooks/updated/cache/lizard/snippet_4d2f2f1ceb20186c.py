def limit_weights(weights, limit=0.1):
    if 1.0 / limit > len(weights):
        raise ValueError('invalid limit -> 1 / limit must be <= len(weights)')
    if isinstance(weights, dict):
        weights = pd.Series(weights)
    if np.round(weights.sum(), 1) != 1.0:
        raise ValueError('Expecting weights (that sum to 1) - sum is %s' %
            weights.sum())
    res = np.round(weights.copy(), 4)
    to_rebalance = (res[res > limit] - limit).sum()
    ok = res[res < limit]
    ok += ok / ok.sum() * to_rebalance
    res[res > limit] = limit
    res[res < limit] = ok
    if any(x > limit for x in res):
        return limit_weights(res, limit=limit)
    return res