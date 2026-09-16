def ensure_shape(core, shape, shape_):
    core = core.copy()
    if shape is None:
        shape = shape_
    elif isinstance(shape, int):
        shape = shape,
    if tuple(shape) == tuple(shape_):
        return core, shape
    ones = np.ones(shape, dtype=int)
    for key, val in core.items():
        core[key] = val * ones
    return core, shape