def _nonzero(self):
    nonzeros = np.nonzero(self.data)
    return tuple(Variable(dim, nz) for nz, dim in zip(nonzeros, self.dims))