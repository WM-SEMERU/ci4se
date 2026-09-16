def eigendecompose(self, normalise=False):
    self.eigenvalues, self.eigenvectors = utils.eigendecompose(self.tensor,
        normalise)
    return self.eigenvalues, self.eigenvectors