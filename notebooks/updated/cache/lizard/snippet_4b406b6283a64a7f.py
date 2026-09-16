def _logpdf(self, **kwargs):
    if kwargs in self:
        return sum([(self._lognorm[p] + self._expnorm[p] * (kwargs[p] -
            self._mean[p]) ** 2.0) for p in self._params])
    else:
        return -numpy.inf