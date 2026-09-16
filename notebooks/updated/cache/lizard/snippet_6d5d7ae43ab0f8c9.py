def _z2deriv(self, R, z, phi=0.0, t=0.0):
    l, n = bovy_coords.Rz_to_lambdanu(R, z, ac=self._ac, Delta=self._Delta)
    jac = bovy_coords.Rz_to_lambdanu_jac(R, z, Delta=self._Delta)
    hess = bovy_coords.Rz_to_lambdanu_hess(R, z, Delta=self._Delta)
    dldz = jac[0, 1]
    dndz = jac[1, 1]
    d2ldz2 = hess[0, 1, 1]
    d2ndz2 = hess[1, 1, 1]
    return d2ldz2 * self._lderiv(l, n) + d2ndz2 * self._nderiv(l, n
        ) + dldz ** 2 * self._l2deriv(l, n) + dndz ** 2 * self._n2deriv(l, n
        ) + 2.0 * dldz * dndz * self._lnderiv(l, n)