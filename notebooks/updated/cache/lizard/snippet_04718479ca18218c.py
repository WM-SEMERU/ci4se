def jukesCantorD(p, L=100):
    assert 0 <= p < 0.75
    rD = 1 - 4.0 / 3 * p
    D = -0.75 * log(rD)
    varD = p * (1 - p) / (rD ** 2 * L)
    return D, varD