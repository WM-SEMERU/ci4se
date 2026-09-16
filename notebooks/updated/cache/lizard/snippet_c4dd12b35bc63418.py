def mean(self, values, axis=0, weights=None, dtype=None):
    values = np.asarray(values)
    if weights is None:
        result = self.reduce(values, axis=axis, dtype=dtype)
        shape = [1] * values.ndim
        shape[axis] = self.groups
        weights = self.count.reshape(shape)
    else:
        weights = np.asarray(weights)
        result = self.reduce(values * weights, axis=axis, dtype=dtype)
        weights = self.reduce(weights, axis=axis, dtype=dtype)
    return self.unique, result / weights