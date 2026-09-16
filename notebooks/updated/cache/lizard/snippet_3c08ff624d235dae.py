def grad(self, X, mean=None, lenscale=None):
    r
    d = X.shape[1]
    mean = self._check_dim(d, mean, paramind=0)
    lenscale = self._check_dim(d, lenscale, paramind=1)
    VX = self._makeVX(X / lenscale)
    mX = X.dot(mean)[:, (np.newaxis)]
    sinVXpmX = -np.sin(VX + mX)
    sinVXmmX = -np.sin(VX - mX)
    cosVXpmX = np.cos(VX + mX)
    cosVXmmX = np.cos(VX - mX)
    dPhi_len = []
    dPhi_mean = []
    for i, l in enumerate(lenscale):
        dmX = X[:, ([i])]
        dPhi_mean.append(np.hstack((dmX * sinVXpmX, dmX * cosVXpmX, -dmX *
            sinVXmmX, -dmX * cosVXmmX)) / np.sqrt(2 * self.n))
        indlen = np.zeros(d)
        indlen[i] = 1.0 / l ** 2
        dVX = -self._makeVX(X * indlen)
        dPhi_len.append(np.hstack((dVX * sinVXpmX, dVX * cosVXpmX, dVX *
            sinVXmmX, dVX * cosVXmmX)) / np.sqrt(2 * self.n))
    dPhi_mean = np.dstack(dPhi_mean) if d != 1 else dPhi_mean[0]
    dPhi_len = np.dstack(dPhi_len) if d != 1 else dPhi_len[0]
    return dPhi_mean, dPhi_len