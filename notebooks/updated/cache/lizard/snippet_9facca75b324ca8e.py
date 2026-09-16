def feedforward(self):
    m = self._numInputs
    n = self._numColumns
    W = np.zeros((n, m))
    for i in range(self._numColumns):
        self.getPermanence(i, W[(i), :])
    return W