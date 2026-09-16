def dimension_sort(odict, kdims, vdims, key_index):
    sortkws = {}
    ndims = len(kdims)
    dimensions = kdims + vdims
    indexes = [(dimensions[i], int(i not in range(ndims)), i if i in range(
        ndims) else i - ndims) for i in key_index]
    cached_values = {d.name: ([None] + list(d.values)) for d in dimensions}
    if len(set(key_index)) != len(key_index):
        raise ValueError('Cannot sort on duplicated dimensions')
    else:
        sortkws['key'] = lambda x: tuple(cached_values[dim.name].index(x[t]
            [d]) if dim.values else x[t][d] for i, (dim, t, d) in enumerate
            (indexes))
    if sys.version_info.major == 3:
        return python2sort(odict.items(), **sortkws)
    else:
        return sorted(odict.items(), **sortkws)