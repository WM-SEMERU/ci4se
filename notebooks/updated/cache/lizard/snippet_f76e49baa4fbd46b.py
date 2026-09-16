def _internal2external_func(bounds):
    ls = [_internal2external_lambda(b) for b in bounds]

    def convert_i2e(xi):
        xe = empty_like(xi)
        xe[:] = [l(p) for l, p in zip(ls, xi)]
        return xe
    return convert_i2e