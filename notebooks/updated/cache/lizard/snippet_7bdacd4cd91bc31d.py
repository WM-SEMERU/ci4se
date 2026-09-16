def repeat_to_match_shape(g, shape, dtype, axis, keepdims):
    if shape == ():
        return g, 1
    axis = list(axis) if isinstance(axis, tuple) else axis
    new_shape = onp.array(shape)
    new_shape[axis] = 1
    num_reps = onp.prod(onp.array(shape)[axis])
    return anp.reshape(g, new_shape) + onp.zeros(shape, dtype=dtype), num_reps