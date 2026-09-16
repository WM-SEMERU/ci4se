def logpdf_link(self, link_f, y, Y_metadata=None):
    assert np.atleast_1d(link_f).shape == np.atleast_1d(y).shape
    c = np.zeros_like(y)
    if Y_metadata is not None and 'censored' in Y_metadata.keys():
        c = Y_metadata['censored']
    uncensored = (1 - c) * (-0.5 * np.log(2 * np.pi * self.variance) - np.
        log(y) - (np.log(y) - link_f) ** 2 / (2 * self.variance))
    censored = c * np.log(1 - stats.norm.cdf((np.log(y) - link_f) / np.sqrt
        (self.variance)))
    logpdf = uncensored + censored
    return logpdf