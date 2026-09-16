def _iadd_spmatrix(self, X, alpha=1.0):
    assert self.is_factor is False, 'cannot add spmatrix to a cspmatrix factor'
    n = self.symb.n
    snptr = self.symb.snptr
    snode = self.symb.snode
    relptr = self.symb.relptr
    snrowidx = self.symb.snrowidx
    sncolptr = self.symb.sncolptr
    blkptr = self.symb.blkptr
    blkval = self.blkval
    if self.symb.p is not None:
        Xp = tril(perm(symmetrize(X), self.symb.p))
    else:
        Xp = tril(X)
    cp, ri, val = Xp.CCS
    for k in range(self.symb.Nsn):
        nn = snptr[k + 1] - snptr[k]
        na = relptr[k + 1] - relptr[k]
        nj = nn + na
        r = list(snrowidx[sncolptr[k]:sncolptr[k + 1]])
        for i in range(nn):
            j = snode[snptr[k] + i]
            offset = blkptr[k] + nj * i
            I = [(offset + r.index(idx)) for idx in ri[cp[j]:cp[j + 1]]]
            blkval[I] += alpha * val[cp[j]:cp[j + 1]]
    return