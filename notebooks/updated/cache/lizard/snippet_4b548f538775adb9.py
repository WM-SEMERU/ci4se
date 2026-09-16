def dimension(self):
    if self.dim > -1:
        return self.dim
    d = None
    if self.dim != -1 and not self._estimated:
        d = self.dim
    elif self._estimated:
        dim = len(self.eigenvalues)
        if self.var_cutoff < 1.0:
            dim = min(dim, np.searchsorted(self.cumvar, self.var_cutoff) + 1)
        d = dim
    elif self.var_cutoff == 1.0:
        d = self.data_producer.dimension()
    else:
        raise RuntimeError(
            'Requested dimension, but the dimension depends on the cumulative variance and the transformer has not yet been estimated. Call estimate() before.'
            )
    return d