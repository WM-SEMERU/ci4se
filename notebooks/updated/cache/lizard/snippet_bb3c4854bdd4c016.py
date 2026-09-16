def median(self, default=None):
    return numpy.asscalar(numpy.median(self.values)
        ) if self.values else default