def infer_x(self, y):
    assert len(y
        ) == self.fmodel.dim_y, 'Wrong dimension for y. Expected %i, got %i' % (
        self.fmodel.dim_y, len(y))
    if len(self.fmodel.dataset) == 0:
        return [[0.0] * self.dim_x]
    else:
        dists, index = self.fmodel.dataset.nn_y(y, k=self.k)
        w = self._weights(dists, index)
        idx = index[np.argmax(w)]
        return [self.fmodel.dataset.get_x(idx)]