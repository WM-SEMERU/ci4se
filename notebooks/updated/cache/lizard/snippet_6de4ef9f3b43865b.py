def mat2d_window_from_indices(mat, row_indices=None, col_indices=None, copy
    =False):
    if not isinstance(mat, np.ndarray) or mat.ndim != 2:
        raise ValueError('`mat` must be a 2D NumPy array')
    if mat.shape[0] == 0 or mat.shape[1] == 0:
        raise ValueError('invalid shape for `mat`: %s' % mat.shape)
    if row_indices is None:
        row_indices = slice(None)
    elif len(row_indices) == 0:
        raise ValueError('`row_indices` must be non-empty')
    if col_indices is None:
        col_indices = slice(None)
    elif len(col_indices) == 0:
        raise ValueError('`col_indices` must be non-empty')
    view = mat[(row_indices), :][:, (col_indices)]
    if copy:
        return view.copy()
    else:
        return view