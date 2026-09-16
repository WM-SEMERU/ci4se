def initialize(self, endog, freq_weights):
    if endog.ndim > 1 and endog.shape[1] > 1:
        y = endog[:, (0)]
        self.n = endog.sum(1)
        return y * 1.0 / self.n, self.n
    else:
        return endog, np.ones(endog.shape[0])