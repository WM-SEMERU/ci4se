def sum(self, weights=None):
    if weights is None:
        weights = self.data.weights
    return utils.bincount(self.labels, weights, self.N)