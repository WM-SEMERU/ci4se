def is_bool_matrix(l):
    r
    if isinstance(l, np.ndarray):
        if l.ndim == 2 and l.dtype == bool:
            return True
    return False