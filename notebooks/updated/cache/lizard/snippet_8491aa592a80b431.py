def likelihood(x, m=None, Cinv=None, sigma=1, detC=None):
    if m is None:
        dx = x
    else:
        dx = x - m
    n = len(x)
    s2pi = (2 * np.pi) ** (n / 2.0)
    if Cinv is None:
        return exp(-sum(dx ** 2) / sigma ** 2 / 2) / s2pi / sigma ** n
    if detC is None:
        detC = 1.0 / np.linalg.linalg.det(Cinv)
    return exp(-np.dot(dx, np.dot(Cinv, dx)) / sigma ** 2 / 2) / s2pi / abs(
        detC) ** 0.5 / sigma ** n