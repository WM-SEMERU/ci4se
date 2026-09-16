def check_array(array, accept_sparse=None, dtype='numeric', order=None,
    copy=False, force_all_finite=True, ensure_2d=True, allow_nd=False,
    ensure_min_samples=1, ensure_min_features=1):
    if isinstance(accept_sparse, str):
        accept_sparse = [accept_sparse]
    dtype_numeric = dtype == 'numeric'
    if sp.issparse(array):
        if dtype_numeric:
            dtype = None
        array = _ensure_sparse_format(array, accept_sparse, dtype, order,
            copy, force_all_finite)
    else:
        if ensure_2d:
            array = np.atleast_2d(array)
        if dtype_numeric:
            if hasattr(array, 'dtype') and getattr(array.dtype, 'kind', None
                ) == 'O':
                dtype = np.float64
            else:
                dtype = None
        array = np.array(array, dtype=dtype, order=order, copy=copy)
        if dtype_numeric and array.dtype.kind == 'O':
            array = array.astype(np.float64)
        if not allow_nd and array.ndim >= 3:
            raise ValueError('Found array with dim %d. Expected <= 2' %
                array.ndim)
        if force_all_finite:
            _assert_all_finite(array)
    shape_repr = _shape_repr(array.shape)
    if ensure_min_samples > 0:
        n_samples = _num_samples(array)
        if n_samples < ensure_min_samples:
            raise ValueError(
                'Found array with %d sample(s) (shape=%s) while a minimum of %d is required.'
                 % (n_samples, shape_repr, ensure_min_samples))
    if ensure_min_features > 0 and array.ndim == 2:
        n_features = array.shape[1]
        if n_features < ensure_min_features:
            raise ValueError(
                'Found array with %d feature(s) (shape=%s) while a minimum of %d is required.'
                 % (n_features, shape_repr, ensure_min_features))
    return array