def astype(array, y):
    if isinstance(y, autograd.core.Node):
        return array.astype(numpy.array(y.value).dtype)
    return array.astype(numpy.array(y).dtype)