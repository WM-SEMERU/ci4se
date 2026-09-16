def ptdAngle(self, t, dangle):
    if isinstance(t, (int, float, numpy.float32, numpy.float64)):
        t = numpy.array([t])
    out = numpy.zeros(len(t))
    if t > 0.0:
        dO = dangle / t[t < self._tdisrupt]
    else:
        return 0.0
    out[t < self._tdisrupt] = dO ** 2.0 / dangle * numpy.exp(-0.5 * (dO -
        self._meandO) ** 2.0 / self._sortedSigOEig[2]) / numpy.sqrt(self.
        _sortedSigOEig[2])
    return out