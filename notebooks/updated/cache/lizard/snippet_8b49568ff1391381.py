def grad(self, X, lenscale=None):
    r
    d = X.shape[1]
    lenscale = self._check_dim(d, lenscale)
    VX = self._makeVX(X / lenscale)
    sinVX = -np.sin(VX)
    cosVX = np.cos(VX)
    dPhi = []
    for i, l in enumerate(lenscale):
        indlen = np.zeros(d)
        indlen[i] = 1.0 / l ** 2
        dVX = -self._makeVX(X * indlen)
        dPhi.append(np.hstack((dVX * sinVX, dVX * cosVX)) / np.sqrt(self.n))
    return np.dstack(dPhi) if len(lenscale) != 1 else dPhi[0]