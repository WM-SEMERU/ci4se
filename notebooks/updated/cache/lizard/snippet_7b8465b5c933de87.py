def total_weight(self):
    weights = self._raw_weights()
    if weights.shape[1] == 0:
        return 0.0
    elif weights.shape[1] < self._ntaps:
        return np.sum(np.mean(weights, axis=1))
    else:
        return self._filter_coeffs.dot(np.sum(weights, axis=0))