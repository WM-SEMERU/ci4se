def initialize_weights(self):
    n = self._outputSize
    m = self._inputSize
    self._Q = self._random.sample((n, m))
    for i in range(n):
        self._Q[i] /= np.sqrt(np.dot(self._Q[i], self._Q[i]))