def putdata(self, value, blc=(), trc=(), inc=()):
    return self._putdata(value, self._adjustBlc(blc), self._adjustInc(inc))