def loglike(self, endog, mu, freq_weights=1.0, scale=1.0):
    r
    loglike = np.sum(freq_weights * (endog * np.log(mu) - mu - special.
        gammaln(endog + 1)))
    return scale * loglike