def lnLambda(self, r, v):
    if self._lnLambda:
        lnLambda = self._lnLambda
    else:
        GMvs = self._ms / v ** 2.0
        if GMvs < self._rhm:
            Lambda = r / self._gamma / self._rhm
        else:
            Lambda = r / self._gamma / GMvs
        lnLambda = 0.5 * numpy.log(1.0 + Lambda ** 2.0)
    return lnLambda