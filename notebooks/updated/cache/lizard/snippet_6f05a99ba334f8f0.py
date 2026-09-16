def kld(p1, p2):
    return np.sum(np.where(p1 != 0, p1 * np.log(p1 / p2), 0))