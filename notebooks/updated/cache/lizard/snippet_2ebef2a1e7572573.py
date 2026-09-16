def transform(self, values):
    assert self.cdf is not None
    assert self.bin_edges is not None
    indices = numpy.searchsorted(self.bin_edges, values)
    result = self.cdf[indices]
    assert len(result) == len(values)
    return numpy.minimum(result, 100.0)