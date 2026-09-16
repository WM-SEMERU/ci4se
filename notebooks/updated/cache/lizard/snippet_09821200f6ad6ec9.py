def _marginal_loglike(self, x):
    yedge = self._nuis_pdf.marginalization_bins()
    yw = yedge[1:] - yedge[:-1]
    yc = 0.5 * (yedge[1:] + yedge[:-1])
    s = self.like(x[:, (np.newaxis)], yc[(np.newaxis), :])
    z = 1.0 * np.sum(s * yw, axis=1)
    self._marg_z = np.zeros(z.shape)
    msk = z > 0
    self._marg_z[msk] = -1 * np.log(z[msk])
    dlogzdx = (np.log(z[msk][-1]) - np.log(z[msk][-2])) / (x[msk][-1] - x[
        msk][-2])
    self._marg_z[~msk] = self._marg_z[msk][-1] + (self._marg_z[~msk] - self
        ._marg_z[msk][-1]) * dlogzdx
    self._marg_interp = castro.Interpolator(x, self._marg_z)
    return self._marg_z