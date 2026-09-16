def check_initializers(initializers, keys):
    if initializers is None:
        return {}
    _assert_is_dictlike(initializers, valid_keys=keys)
    keys = set(keys)
    if not set(initializers) <= keys:
        extra_keys = set(initializers) - keys
        raise KeyError(
            'Invalid initializer keys {}, initializers can only be provided for {}'
            .format(', '.join("'{}'".format(key) for key in extra_keys),
            ', '.join("'{}'".format(key) for key in keys)))
    _check_nested_callables(initializers, 'Initializer')
    return dict(initializers)