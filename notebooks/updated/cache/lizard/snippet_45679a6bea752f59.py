def _F(self, X, tau):
    t2 = tau ** 2
    _F = self.F(X)
    a = t2 * (t2 + 1) ** -2
    if isinstance(X, np.ndarray):
        b = np.ones_like(X)
        b[X == 1] = (t2 + 1) * 1.0 / 3
        b[X != 1] = (t2 + 1) * (X[X != 1] ** 2 - 1) ** -1 * (1 - _F[X != 1])
    elif isinstance(X, float) or isinstance(X, int):
        if X == 1:
            b = (t2 + 1) * 1.0 / 3
        else:
            b = (t2 + 1) * (X ** 2 - 1) ** -1 * (1 - _F)
    else:
        raise ValueError(
            "The variable type is not compatible with the function, please use float, int or ndarray's."
            )
    c = 2 * _F
    d = -np.pi * (t2 + X ** 2) ** -0.5
    e = (t2 - 1) * (tau * (t2 + X ** 2) ** 0.5) ** -1 * self.L(X, tau)
    result = a * (b + c + d + e)
    return result