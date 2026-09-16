def setup_coords(arr_names=None, sort=[], dims={}, **kwargs):
    try:
        return OrderedDict(arr_names)
    except (ValueError, TypeError):
        pass
    if arr_names is None:
        arr_names = repeat('arr{0}')
    elif isstring(arr_names):
        arr_names = repeat(arr_names)
    dims = OrderedDict(dims)
    for key, val in six.iteritems(kwargs):
        dims.setdefault(key, val)
    sorted_dims = OrderedDict()
    if sort:
        for key in sort:
            sorted_dims[key] = dims.pop(key)
        for key, val in six.iteritems(dims):
            sorted_dims[key] = val
    else:
        if 'name' in dims:
            sorted_dims['name'] = None
        for key, val in sorted(dims.items()):
            sorted_dims[key] = val
        for key, val in six.iteritems(kwargs):
            sorted_dims.setdefault(key, val)
    for key, val in six.iteritems(sorted_dims):
        sorted_dims[key] = iter(safe_list(val))
    return OrderedDict([(arr_name.format(i), dict(zip(sorted_dims.keys(),
        dim_tuple))) for i, (arr_name, dim_tuple) in enumerate(zip(
        arr_names, product(*map(list, sorted_dims.values()))))])