def fgrad_y(self, y, return_precalc=False):
    d = self.d
    mpsi = self.psi
    S = (mpsi[:, (1)] * (y[:, :, (None)] + mpsi[:, (2)])).T
    R = np.tanh(S)
    D = 1 - R ** 2
    GRAD = (d + (mpsi[:, 0:1][:, :, (None)] * mpsi[:, 1:2][:, :, (None)] *
        D).sum(axis=0)).T
    if return_precalc:
        return GRAD, S, R, D
    return GRAD