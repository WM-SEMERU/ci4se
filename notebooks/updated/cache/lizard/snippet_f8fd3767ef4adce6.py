def join_list(values, delimiter=', ', transform=None):
    if transform is None:
        transform = _identity
    if values is not None and not isinstance(values, (str, bytes)):
        values = delimiter.join(transform(x) for x in values)
    return values