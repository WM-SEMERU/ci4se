def dtype_repr(dtype):
    dtype = np.dtype(dtype)
    if dtype == np.dtype(int):
        return "'int'"
    elif dtype == np.dtype(float):
        return "'float'"
    elif dtype == np.dtype(complex):
        return "'complex'"
    elif dtype.shape:
        return "('{}', {})".format(dtype.base, dtype.shape)
    else:
        return "'{}'".format(dtype)