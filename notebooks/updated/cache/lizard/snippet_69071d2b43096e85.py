def reconstruct(self, b, X=None):
    if X is None:
        X = self.getcoef()
    Xf = sl.rfftn(X, None, self.cbpdn.cri.axisN)
    slc = (slice(None),) * self.dimN + (slice(self.chncs[b], self.chncs[b +
        1]),)
    Sf = np.sum(self.cbpdn.Df[slc] * Xf, axis=self.cbpdn.cri.axisM)
    return sl.irfftn(Sf, self.cbpdn.cri.Nv, self.cbpdn.cri.axisN)