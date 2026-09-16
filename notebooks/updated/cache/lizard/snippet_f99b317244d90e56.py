def deviance(self, endog, mu, freq_weights=1.0, scale=1.0):
    return np.sum(freq_weights * (endog - mu) ** 2) / scale