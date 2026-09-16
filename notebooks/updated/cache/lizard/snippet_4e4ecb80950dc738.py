def set_adaptive(self, value: bool=True):
    if value and not self.adaptive_allowed:
        raise RuntimeError('Cannot change binning to adaptive.')
    self._adaptive = value