def fit(self, conver=DEFAULT_CONVERGENCE, minit=DEFAULT_MINIT, maxit=
    DEFAULT_MAXIT, fflag=DEFAULT_FFLAG, maxgerr=DEFAULT_MAXGERR,
    going_inwards=False):
    self._sample.update()
    return CentralPixel(self._sample)