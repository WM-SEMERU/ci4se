def compute_laplacian_matrix(self, copy=True, return_lapsym=False, **kwargs):
    if self.affinity_matrix is None:
        self.compute_affinity_matrix()
    kwds = self.laplacian_kwds.copy()
    kwds.update(kwargs)
    kwds['full_output'] = return_lapsym
    result = compute_laplacian_matrix(self.affinity_matrix, self.
        laplacian_method, **kwds)
    if return_lapsym:
        (self.laplacian_matrix, self.laplacian_symmetric, self.
            laplacian_weights) = result
    else:
        self.laplacian_matrix = result
    if copy:
        return self.laplacian_matrix.copy()
    else:
        return self.laplacian_matrix