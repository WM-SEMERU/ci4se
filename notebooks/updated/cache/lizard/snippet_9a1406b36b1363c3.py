def _checkDimensionsListLike(arrays):
    dim1 = len(arrays)
    dim2, dim3 = arrays[0].shape
    for aa in range(1, dim1):
        dim2_aa, dim3_aa = arrays[aa].shape
        if dim2_aa != dim2 or dim3_aa != dim3:
            raise _error.InvalidError(_MDPERR['obj_square'])
    return dim1, dim2, dim3