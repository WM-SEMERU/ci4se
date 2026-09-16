def LogLikelihood(self, data):
    m = len(data)
    if self.n < m:
        return float('-inf')
    x = self.Random()
    y = numpy.log(x[:m]) * data
    return y.sum()