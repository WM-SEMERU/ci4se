def num_compositions(m, n):
    return scipy.special.comb(n + m - 1, m - 1, exact=True)