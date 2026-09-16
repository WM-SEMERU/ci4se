def apply(self, func, shortcut=False, args=(), **kwargs):
    combined = super(DataArrayResample, self).apply(func, shortcut=shortcut,
        args=args, **kwargs)
    if self._dim in combined.coords:
        combined = combined.drop(self._dim)
    if self._resample_dim in combined.dims:
        combined = combined.rename({self._resample_dim: self._dim})
    return combined