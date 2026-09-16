def stdev(self, default=None):
    return numpy.asscalar(numpy.std(self.values)) if self.values else default