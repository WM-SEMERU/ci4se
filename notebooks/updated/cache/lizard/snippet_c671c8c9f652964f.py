def register(self, field, shape, dtype):
    if not isinstance(dtype, type):
        raise ParameterError('dtype={} must be a type'.format(dtype))
    if not (isinstance(shape, Iterable) and all([(s is None or isinstance(s,
        int)) for s in shape])):
        raise ParameterError('shape={} must be an iterable of integers'.
            format(shape))
    self.fields[self.scope(field)] = Tensor(tuple(shape), dtype)