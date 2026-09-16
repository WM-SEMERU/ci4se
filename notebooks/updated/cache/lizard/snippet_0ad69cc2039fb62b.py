def endpoint_iter(self, *dim_strides, **kwargs):

    def _dim_endpoints(size, stride):
        r = xrange(0, size, stride) if stride > 0 else xrange(0, size)
        return ((i, min(i + stride, size)) for i in r)
    dims = self.dimensions(copy=False)
    gens = (_dim_endpoints(dims[d].global_size, s) for d, s in dim_strides)
    return itertools.product(*gens)