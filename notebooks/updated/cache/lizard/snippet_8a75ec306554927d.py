def _slice2rows(self, start, stop, step=None):
    nrows = self._info['nrows']
    if start is None:
        start = 0
    if stop is None:
        stop = nrows
    if step is None:
        step = 1
    tstart = self._fix_range(start)
    tstop = self._fix_range(stop)
    if tstart == 0 and tstop == nrows:
        return None
    if stop < start:
        raise ValueError('start is greater than stop in slice')
    return numpy.arange(tstart, tstop, step, dtype='i8')