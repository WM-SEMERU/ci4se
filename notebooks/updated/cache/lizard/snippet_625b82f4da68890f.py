def evaluate(self, x, y, flux, x_0, y_0):
    x = (x - x_0 + 0.5 + self.prf_shape[1] // 2).astype('int')
    y = (y - y_0 + 0.5 + self.prf_shape[0] // 2).astype('int')
    y_sub, x_sub = subpixel_indices((y_0, x_0), self.subsampling)
    x_bound = np.logical_or(x < 0, x >= self.prf_shape[1])
    y_bound = np.logical_or(y < 0, y >= self.prf_shape[0])
    out_of_bounds = np.logical_or(x_bound, y_bound)
    x[x_bound] = 0
    y[y_bound] = 0
    result = flux * self._prf_array[int(y_sub), int(x_sub)][y, x]
    result[out_of_bounds] = 0
    return result