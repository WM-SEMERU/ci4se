def is_npvalue(u, dtype):
    if is_quantity(u):
        return is_npvalue(mag(u), dtype=dtype)
    return any(np.issubdtype(type(u), np.generic if d is None else d) for d in
        numpy_type(dtype))