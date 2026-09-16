def M(self, t, tips=None, gaps=None):
    assert isinstance(t, float) and t > 0, 'Invalid t: {0}'.format(t)
    with scipy.errstate(under='ignore'):
        if ('expD', t) not in self._cached:
            self._cached['expD', t] = scipy.exp(self.D * self.mu * t)
        expD = self._cached['expD', t]
        if tips is None:
            M = broadcastMatrixMultiply((self.A.swapaxes(0, 1) * expD).
                swapaxes(1, 0), self.Ainv)
        else:
            M = broadcastMatrixVectorMultiply((self.A.swapaxes(0, 1) * expD
                ).swapaxes(1, 0), broadcastGetCols(self.Ainv, tips))
            if gaps is not None:
                M[gaps] = scipy.ones(N_CODON, dtype='float')
    M[M < 0] = 0.0
    return M