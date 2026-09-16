def _nanmedian(array, axis=None):
    if isinstance(axis, tuple):
        array = _move_tuple_axes_first(array, axis=axis)
        axis = 0
    return bottleneck.nanmedian(array, axis=axis)