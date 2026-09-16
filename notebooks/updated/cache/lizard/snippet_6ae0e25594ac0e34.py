def _inner(x, y, axis=-1):
    return cp.sum(x * y, axis=axis, keepdims=True)