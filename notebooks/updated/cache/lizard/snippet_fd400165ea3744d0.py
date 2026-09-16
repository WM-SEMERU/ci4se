def check_data(cls, name, dims, is_unstructured):
    if isinstance(name, six.string_types) or not is_iterable(name):
        name = [name]
        dims = [dims]
        is_unstructured = [is_unstructured]
    N = len(name)
    if N != 1:
        return [False] * N, ['Number of provided names (%i) must equal 1!' % N
            ] * N
    elif len(dims) != 1:
        return [False], [
            'Number of provided dimension lists (%i) must equal 1!' % len(dims)
            ]
    elif len(is_unstructured) != 1:
        return [False], [
            'Number of provided unstructured information (%i) must equal 1!' %
            len(is_unstructured)]
    if name[0] != 0 and not name[0]:
        return [False], ['At least one variable name must be provided!']
    dimlen = cls.allowed_dims
    if is_unstructured[0]:
        dimlen -= 1
    if not isstring(name[0]) and not is_iterable(name[0]) and len(name[0]
        ) != 1 and len(dims[0]) != dimlen - 1:
        return [False], ['Only one name is allowed per array!']
    if len(dims[0]) != dimlen:
        return [False], ['An array with dimension %i is required, not %i' %
            (dimlen, len(dims[0]))]
    return [True], ['']