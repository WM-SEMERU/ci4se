def _call(self, x):
    y = np.bincount(self._indices_flat, weights=x, minlength=self.range.size)
    out = y.reshape(self.range.shape)
    if self.variant == 'dirac':
        weights = getattr(self.range, 'cell_volume', 1.0)
    elif self.variant == 'char_fun':
        weights = 1.0
    else:
        raise RuntimeError('The variant "{!r}" is not yet supported'.format
            (self.variant))
    if weights != 1.0:
        out /= weights
    return out