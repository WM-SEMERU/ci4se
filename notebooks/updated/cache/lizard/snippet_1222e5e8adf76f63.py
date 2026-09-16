def init_fftw_plan(self, planning_effort='measure', **kwargs):
    if self.impl != 'pyfftw':
        raise ValueError('cannot create fftw plan without fftw backend')
    inverse = isinstance(self, FourierTransformInverse)
    if inverse:
        rspace = self.range
        fspace = self.domain
    else:
        rspace = self.domain
        fspace = self.range
    if rspace.field == ComplexNumbers():
        if self._tmp_r is not None:
            arr_in = arr_out = self._tmp_r
        elif self._tmp_f is not None:
            arr_in = arr_out = self._tmp_f
        else:
            arr_in = arr_out = rspace.element().asarray()
    elif self.halfcomplex:
        if self._tmp_r is not None:
            arr_r = self._tmp_r
        else:
            arr_r = rspace.element().asarray()
        if self._tmp_f is not None:
            arr_f = self._tmp_f
        else:
            arr_f = fspace.element().asarray()
        if inverse:
            arr_in, arr_out = arr_f, arr_r
        else:
            arr_in, arr_out = arr_r, arr_f
    elif self._tmp_f is not None:
        arr_in = arr_out = self._tmp_f
    else:
        arr_in = arr_out = fspace.element().asarray()
    kwargs.pop('planning_timelimit', None)
    direction = 'forward' if self.sign == '-' else 'backward'
    self._fftw_plan = pyfftw_call(arr_in, arr_out, direction=direction,
        halfcomplex=self.halfcomplex, axes=self.axes, planning_effort=
        planning_effort, **kwargs)