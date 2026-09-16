def integrate(self, min, max, attr=None, info={}):
    if numpy.isscalar(min):
        min = [min for i in range(self.ndims)]
    if numpy.isscalar(max):
        max = [max for i in range(self.ndims)]
    min = numpy.array(min, dtype='f8', order='C')
    max = numpy.array(max, dtype='f8', order='C')
    if min.shape[-1] != self.ndims:
        raise ValueError('dimension of min does not match Node')
    if max.shape[-1] != self.ndims:
        raise ValueError('dimension of max does not match Node')
    min, max = broadcast_arrays(min, max)
    return _core.KDNode.integrate(self, min, max, attr, info)