def get_dim_name(arr, names):
    for name in names:
        if hasattr(arr, name):
            return name
    raise AttributeError(
        'No attributes of the object `{0}` match the specified names of `{1}`'
        .format(arr, names))