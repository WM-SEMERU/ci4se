def estimate(self, observations, weights):
    N = self.nstates
    K = len(observations)
    self._means = np.zeros(N)
    w_sum = np.zeros(N)
    for k in range(K):
        for i in range(N):
            self.means[i] += np.dot(weights[k][:, (i)], observations[k])
        w_sum += np.sum(weights[k], axis=0)
    self._means /= w_sum
    self._sigmas = np.zeros(N)
    w_sum = np.zeros(N)
    for k in range(K):
        for i in range(N):
            Y = (observations[k] - self.means[i]) ** 2
            self.sigmas[i] += np.dot(weights[k][:, (i)], Y)
        w_sum += np.sum(weights[k], axis=0)
    self._sigmas /= w_sum
    self._sigmas = np.sqrt(self.sigmas)
    if np.any(self._sigmas < np.finfo(self._sigmas.dtype).eps):
        raise RuntimeError('at least one sigma is too small to continue.')