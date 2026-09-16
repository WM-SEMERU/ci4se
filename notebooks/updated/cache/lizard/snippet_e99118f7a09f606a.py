def _concat_compat(to_concat, axis=0):

    def is_nonempty(x):
        try:
            return x.shape[axis] > 0
        except Exception:
            return True
    typs = get_dtype_kinds(to_concat)
    _contains_datetime = any(typ.startswith('datetime') for typ in typs)
    _contains_period = any(typ.startswith('period') for typ in typs)
    if 'category' in typs:
        return _concat_categorical(to_concat, axis=axis)
    elif _contains_datetime or 'timedelta' in typs or _contains_period:
        return _concat_datetime(to_concat, axis=axis, typs=typs)
    elif 'sparse' in typs:
        return _concat_sparse(to_concat, axis=axis, typs=typs)
    all_empty = all(not is_nonempty(x) for x in to_concat)
    if any(is_extension_array_dtype(x) for x in to_concat) and axis == 1:
        to_concat = [np.atleast_2d(x.astype('object')) for x in to_concat]
    if all_empty:
        typs = get_dtype_kinds(to_concat)
        if len(typs) != 1:
            if not len(typs - {'i', 'u', 'f'}) or not len(typs - {'bool',
                'i', 'u'}):
                pass
            else:
                to_concat = [x.astype('object') for x in to_concat]
    return np.concatenate(to_concat, axis=axis)