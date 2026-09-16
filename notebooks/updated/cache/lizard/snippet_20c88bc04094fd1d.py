def P(self, value):
    self._P = value
    self._P1_2 = cholesky(self._P, lower=True)