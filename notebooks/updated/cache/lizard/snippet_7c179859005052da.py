def change_ref(self, gm=None, r0=None, lmax=None):
    if lmax is None:
        lmax = self.lmax
    clm = self.pad(lmax)
    if gm is not None and gm != self.gm:
        clm.coeffs *= self.gm / gm
        clm.gm = gm
        if self.errors is not None:
            clm.errors *= self.gm / gm
    if r0 is not None and r0 != self.r0:
        for l in _np.arange(lmax + 1):
            clm.coeffs[:, (l), :l + 1] *= (self.r0 / r0) ** l
            if self.errors is not None:
                clm.errors[:, (l), :l + 1] *= (self.r0 / r0) ** l
        clm.r0 = r0
    return clm