def _preprocess(self, x, out=None):
    if out is None:
        if self.domain.field == ComplexNumbers():
            out = self._tmp_r if self._tmp_r is not None else self._tmp_f
        elif self.domain.field == RealNumbers() and not self.halfcomplex:
            out = self._tmp_f
        else:
            out = self._tmp_r
    return dft_preprocess_data(x, shift=self.shifts, axes=self.axes, sign=
        self.sign, out=out)