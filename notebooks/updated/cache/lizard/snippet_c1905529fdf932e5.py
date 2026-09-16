def gamma_statistic(self):
    t = copy(self)
    t.resolve_polytomies()
    G = [g for g in t.coalescence_times(backward=False)]
    n = len(G) + 1
    if n <= 2:
        raise RuntimeError(
            'Gamma statistic can only be computed on trees with more than 2 leaves'
            )
    T = sum((j + 2) * g for j, g in enumerate(G))
    out = 0.0
    for i in range(len(G) - 1):
        for k in range(i + 1):
            out += (k + 2) * G[k]
    out /= n - 2
    out -= T / 2
    out /= T
    out /= (1.0 / (12 * (n - 2))) ** 0.5
    return out