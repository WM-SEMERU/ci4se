def is_timeseries(nc, variable):
    dims = nc.variables[variable].dimensions
    cmatrix = coordinate_dimension_matrix(nc)
    time_variables = get_time_variables(nc)
    if len(dims) != 1:
        return False
    dim = dims[0]
    if dim not in time_variables:
        return False
    if 'x' in cmatrix:
        if len(cmatrix['x']) != 0:
            return False
    if 'y' in cmatrix:
        if len(cmatrix['y']) != 0:
            return False
    if 'z' in cmatrix:
        if len(cmatrix['z']) != 0:
            return False
    return True