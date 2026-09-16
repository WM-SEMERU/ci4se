def _reduce(self, func, axis=0):
    if self.mode == 'local':
        axes = sorted(tupleize(axis))
        if isinstance(func, ufunc):
            inshape(self.shape, axes)
            reduced = func.reduce(self, axis=tuple(axes))
        else:
            reshaped = self._align(axes)
            reduced = reduce(func, reshaped)
        expected_shape = [self.shape[i] for i in range(len(self.shape)) if 
            i not in axes]
        if reduced.shape != tuple(expected_shape):
            raise ValueError(
                'reduce did not yield an array with valid dimensions')
        return self._constructor(reduced[(newaxis), :]).__finalize__(self)
    if self.mode == 'spark':
        reduced = self.values.reduce(func, axis, keepdims=True)
        return self._constructor(reduced).__finalize__(self)