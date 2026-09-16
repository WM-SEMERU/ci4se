def symmetrify(A, upper=False):
    if use_linalg_cython:
        _symmetrify_cython(A, upper)
    else:
        _symmetrify_numpy(A, upper)