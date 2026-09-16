def _make_rank(dist_obj, n, mu, sigma, crit=0.5, upper=10000, xtol=1):
    qs = (np.arange(1, n + 1) - 0.5) / n
    rank = np.empty(len(qs))
    brute_ppf = lambda val, prob: prob - dist_obj.cdf(val, mu, sigma)
    qs_less = qs <= crit
    ind = np.sum(qs_less)
    rank[qs_less] = dist_obj.ppf(qs[qs_less], mu, sigma)
    for i, tq in enumerate(qs[~qs_less]):
        j = ind + i
        try:
            rank[j] = np.abs(np.ceil(optim.brentq(brute_ppf, -1, upper,
                args=(tq,), xtol=xtol)))
        except ValueError:
            rank[j:] = np.repeat(rank[j - 1], len(rank[j:]))
            break
    return rank