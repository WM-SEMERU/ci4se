def is_bool_dtype(arr_or_dtype):
    if arr_or_dtype is None:
        return False
    try:
        dtype = _get_dtype(arr_or_dtype)
    except TypeError:
        return False
    if isinstance(arr_or_dtype, CategoricalDtype):
        arr_or_dtype = arr_or_dtype.categories
    if isinstance(arr_or_dtype, ABCIndexClass):
        return (arr_or_dtype.is_object and arr_or_dtype.inferred_type ==
            'boolean')
    elif is_extension_array_dtype(arr_or_dtype):
        dtype = getattr(arr_or_dtype, 'dtype', arr_or_dtype)
        return dtype._is_boolean
    return issubclass(dtype.type, np.bool_)