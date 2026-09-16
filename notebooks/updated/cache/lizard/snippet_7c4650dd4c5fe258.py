def calcu0(self, E, Lz):
    logu0 = optimize.brent(_u0Eq, args=(self._delta, self._pot, E, Lz ** 
        2.0 / 2.0))
    return numpy.exp(logu0)