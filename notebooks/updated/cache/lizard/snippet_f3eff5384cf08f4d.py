def fs_c_sup(self, DF, N=None):
    if not hasattr(self, 'F'):
        self.fs_r(N=self.rank)
    if N and (not isinstance(N, int) or N <= 0):
        raise ValueError('ncols should be a positive integer.')
    s = -sqrt(self.E) if self.cor else self.s
    N = min(N, self.rank) if N else self.rank
    S_inv = diagsvd(-1 / s[:N], len(self.F.T), N)
    return _mul((DF / DF.sum()).T, self.F, S_inv)[:, :N]