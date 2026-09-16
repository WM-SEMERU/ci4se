def _expectation(p, kern, none1, none2, none3, nghp=None):
    r
    if not kern.on_separate_dimensions:
        raise NotImplementedError(
            'Product currently needs to be defined on separate dimensions.')
    return functools.reduce(tf.multiply, [expectation(p, k, nghp=nghp) for
        k in kern.kernels])