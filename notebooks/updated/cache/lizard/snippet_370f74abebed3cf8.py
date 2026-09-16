def _coupling_matrix(self, lmax, nwin=None, weights=None):
    if nwin is None:
        nwin = self.nwin
    if weights is None:
        weights = self.weights
    tapers_power = _np.zeros((self.lwin + 1, nwin))
    for i in range(nwin):
        tapers_power[:, (i)] = _spectrum(self.to_array(i), normalization=
            '4pi', convention='power', unit='per_l')
    if weights is None:
        return _shtools.SHMTCouplingMatrix(lmax, tapers_power, k=nwin)
    else:
        return _shtools.SHMTCouplingMatrix(lmax, tapers_power, k=nwin,
            taper_wt=self.weights)