def calcEL(self, **kwargs):
    E, L = calcELAxi(self._R, self._vR, self._vT, self._pot)
    if self._gamma != 0.0:
        E -= self._vT ** 2.0 / 2.0
        L = m.fabs(L) + self._gamma * self.Jz(**kwargs)
        E += L ** 2.0 / 2.0 / self._R ** 2.0
    return E, L