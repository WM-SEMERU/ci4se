def is_uniform(keys, axis=semantics.axis_default):
    index = as_index(keys, axis)
    return index.uniform