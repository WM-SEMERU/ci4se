def recomb_probability(cM, method='kosambi'):
    assert method in ('kosambi', 'haldane')
    d = cM / 100.0
    if method == 'kosambi':
        e4d = exp(4 * d)
        return (e4d - 1) / (e4d + 1) / 2
    elif method == 'haldane':
        return (1 - exp(-2 * d)) / 2