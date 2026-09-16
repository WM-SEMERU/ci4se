def vector_is_zero(vector_in, tol=1e-07):
    if not isinstance(vector_in, (list, tuple)):
        raise TypeError('Input vector must be a list or a tuple')
    res = [False for _ in range(len(vector_in))]
    for idx in range(len(vector_in)):
        if abs(vector_in[idx]) < tol:
            res[idx] = True
    return all(res)