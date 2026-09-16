def arrays_to_string(file_prefix=None):
    return Registry(types={numpy.ndarray: SerNumpyArray(), numpy.floating:
        SerNumpyScalar()}, hooks={'<ufunc>': SerUFunc()}, hook_fn=_numpy_hook)