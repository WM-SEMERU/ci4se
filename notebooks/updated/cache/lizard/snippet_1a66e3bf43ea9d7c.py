def _nemo_accpars(self, vo, ro):
    ampl = self._amp * vo ** 2.0 * ro ** (self.alpha - 2.0)
    return '0,%s,%s,%s' % (ampl, self.alpha, self.rc * ro)