def All(a, axis, keep_dims):
    return np.all(a, axis=axis if not isinstance(axis, np.ndarray) else
        tuple(axis), keepdims=keep_dims),