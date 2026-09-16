def conditional_probability_alive(self, frequency, recency, T):
    r, alpha, a, b = self._unload_params('r', 'alpha', 'a', 'b')
    log_div = (r + frequency) * np.log((alpha + T) / (alpha + recency)
        ) + np.log(a / (b + np.maximum(frequency, 1) - 1))
    return np.atleast_1d(np.where(frequency == 0, 1.0, expit(-log_div)))