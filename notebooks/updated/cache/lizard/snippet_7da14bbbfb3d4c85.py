def dict_2_mat(data, fill=True):
    if any([(type(k) != int) for k in list(data.keys())]):
        raise RuntimeError('Dictionary cannot be converted to matrix, ' +
            'not all keys are ints')
    base_shape = np.array(list(data.values())[0]).shape
    result_shape = list(base_shape)
    if fill:
        result_shape.insert(0, max(data.keys()) + 1)
    else:
        result_shape.insert(0, len(list(data.keys())))
    result = np.empty(result_shape) + np.nan
    for i, (k, v) in enumerate(data.items()):
        v = np.array(v)
        if v.shape != base_shape:
            raise RuntimeError('Dictionary cannot be converted to matrix, ' +
                'not all values have same dimensions')
        result[fill and [k][0] or [i][0]] = v
    return result