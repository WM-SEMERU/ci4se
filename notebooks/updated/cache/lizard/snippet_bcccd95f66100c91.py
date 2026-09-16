def sample(self, t=None, size=1):
    if t is None:
        self.recompute()
        n, _ = self._x.shape
        results = self.solver.apply_sqrt(np.random.randn(size, n))
        results += self._call_mean(self._x)
        return results[0] if size == 1 else results
    x = self.parse_samples(t)
    cov = self.get_matrix(x)
    cov[np.diag_indices_from(cov)] += TINY
    return multivariate_gaussian_samples(cov, size, mean=self._call_mean(x))