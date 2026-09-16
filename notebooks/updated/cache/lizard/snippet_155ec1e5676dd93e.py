def _brentq_cdf(self, value):
    bound_cdf = partial(scalarize(GaussianKDE.cumulative_distribution), self)

    def f(x):
        return bound_cdf(x) - value
    return f