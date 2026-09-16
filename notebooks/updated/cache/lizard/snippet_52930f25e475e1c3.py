def xarray_derivative_wrap(func):

    @functools.wraps(func)
    def wrapper(f, **kwargs):
        if 'x' in kwargs or 'delta' in kwargs:
            return preprocess_xarray(func)(f, **kwargs)
        elif isinstance(f, xr.DataArray):
            axis = f.metpy.find_axis_name(kwargs.get('axis', 0))
            new_kwargs = {'axis': f.get_axis_num(axis)}
            if f[axis].attrs.get('_metpy_axis') == 'T':
                new_kwargs['x'] = f[axis].metpy.as_timestamp().metpy.unit_array
            elif CFConventionHandler.check_axis(f[axis], 'lon'):
                new_kwargs['delta'], _ = grid_deltas_from_dataarray(f)
            elif CFConventionHandler.check_axis(f[axis], 'lat'):
                _, new_kwargs['delta'] = grid_deltas_from_dataarray(f)
            else:
                new_kwargs['x'] = f[axis].metpy.unit_array
            result = func(f.metpy.unit_array, **new_kwargs)
            return xr.DataArray(result.magnitude, coords=f.coords, dims=f.
                dims, attrs={'units': str(result.units)})
        else:
            raise ValueError(
                'Must specify either "x" or "delta" for value positions when "f" is not a DataArray.'
                )
    return wrapper