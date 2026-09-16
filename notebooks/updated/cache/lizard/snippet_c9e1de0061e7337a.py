def full(self, asvector=False):
    sz = self.n.copy()
    if self.r[0] > 1:
        sz = _np.concatenate(([self.r[0]], sz))
    if self.r[self.d] > 1:
        sz = _np.concatenate(([self.r[self.d]], sz))
    if _np.iscomplex(self.core).any():
        a = _tt_f90.tt_f90.ztt_to_full(self.n, self.r, self.ps, self.core,
            _np.prod(sz))
    else:
        a = _tt_f90.tt_f90.dtt_to_full(self.n, self.r, self.ps, _np.real(
            self.core), _np.prod(sz))
    a = a.reshape(sz, order='F')
    if asvector:
        a = a.flatten(order='F')
    return a