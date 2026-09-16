def round(self, eps=1e-14, rmax=1000000):
    c = vector()
    c.n = _np.copy(self.n)
    c.d = self.d
    c.r = _np.copy(self.r)
    c.ps = _np.copy(self.ps)
    if _np.iscomplex(self.core).any():
        _tt_f90.tt_f90.ztt_compr2(c.n, c.r, c.ps, self.core, eps, rmax)
        c.core = _tt_f90.tt_f90.zcore.copy()
    else:
        _tt_f90.tt_f90.dtt_compr2(c.n, c.r, c.ps, self.core, eps, rmax)
        c.core = _tt_f90.tt_f90.core.copy()
    _tt_f90.tt_f90.tt_dealloc()
    return c