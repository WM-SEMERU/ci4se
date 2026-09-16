def _d2f(self, x):
    d2f_dPg2 = lil_matrix((self._ng, 1))
    d2f_dQg2 = lil_matrix((self._ng, 1))
    for i in self._ipol:
        p_cost = list(self._gn[i].p_cost)
        d2f_dPg2[i, 0] = polyval(polyder(p_cost, 2), self._Pg.v0[i] * self.
            _base_mva) * self._base_mva ** 2
    i = r_[range(self._Pg.i1, self._Pg.iN + 1), range(self._Qg.i1, self._Qg
        .iN + 1)]
    d2f = csr_matrix((vstack([d2f_dPg2, d2f_dQg2]).toarray().flatten(), (i,
        i)), shape=(self._nxyz, self._nxyz))
    return d2f