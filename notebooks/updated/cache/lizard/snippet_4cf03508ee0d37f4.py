def dict_to_dataset(data, *, attrs=None, library=None, coords=None, dims=None):
    if dims is None:
        dims = {}
    data_vars = {}
    for key, values in data.items():
        data_vars[key] = numpy_to_data_array(values, var_name=key, coords=
            coords, dims=dims.get(key))
    return xr.Dataset(data_vars=data_vars, attrs=make_attrs(attrs=attrs,
        library=library))