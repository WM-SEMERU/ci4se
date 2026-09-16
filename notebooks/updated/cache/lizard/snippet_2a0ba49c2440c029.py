def pdf_link(self, link_f, y, Y_metadata=None):
    assert np.atleast_1d(link_f).shape == np.atleast_1d(y).shape
    alpha = link_f * self.beta
    objective = y ** (alpha - 1.0) * np.exp(-self.beta * y
        ) * self.beta ** alpha / special.gamma(alpha)
    return np.exp(np.sum(np.log(objective)))