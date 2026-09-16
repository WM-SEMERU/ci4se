def stretch_linear(self, cutoffs=(0.005, 0.005)):
    logger.debug('Perform a linear contrast stretch.')
    logger.debug('Calculate the histogram quantiles: ')
    logger.debug('Left and right quantiles: ' + str(cutoffs[0]) + ' ' + str
        (cutoffs[1]))
    cutoff_type = np.float64
    if np.issubdtype(self.data.dtype, np.floating) and np.dtype(self.data.dtype
        ).itemsize > 8:
        cutoff_type = self.data.dtype
    left, right = dask.delayed(self._compute_quantile, nout=2)(self.data.
        data, self.data.dims, cutoffs)
    left_data = da.from_delayed(left, shape=(self.data.sizes['bands'],),
        dtype=cutoff_type)
    left = xr.DataArray(left_data, dims=('bands',), coords={'bands': self.
        data['bands']})
    right_data = da.from_delayed(right, shape=(self.data.sizes['bands'],),
        dtype=cutoff_type)
    right = xr.DataArray(right_data, dims=('bands',), coords={'bands': self
        .data['bands']})
    self.crude_stretch(left, right)