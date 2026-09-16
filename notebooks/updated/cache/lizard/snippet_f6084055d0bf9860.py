def set_adaptive(self, value: bool=True):
    if not all(b.adaptive_allowed for b in self._binnings):
        raise RuntimeError('All binnings must allow adaptive behaviour.')
    for binning in self._binnings:
        binning.set_adaptive(value)