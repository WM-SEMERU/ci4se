def percentile(self, n, default=None):
    return numpy.asscalar(numpy.percentile(self.values, n)
        ) if self.values else default