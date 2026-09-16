def calculate_dimensions(variables):
    dims = OrderedDict()
    last_used = {}
    scalar_vars = set(k for k, v in variables.items() if not v.dims)
    for k, var in variables.items():
        for dim, size in zip(var.dims, var.shape):
            if dim in scalar_vars:
                raise ValueError(
                    'dimension %r already exists as a scalar variable' % dim)
            if dim not in dims:
                dims[dim] = size
                last_used[dim] = k
            elif dims[dim] != size:
                raise ValueError(
                    'conflicting sizes for dimension %r: length %s on %r and length %s on %r'
                     % (dim, size, k, dims[dim], last_used[dim]))
    return dims