def get_callable(key, dct):
    from sklearn.externals import six
    fun = dct.get(key, None)
    if not isinstance(key, six.string_types) or fun is None:
        raise ValueError('key must be a string in one in %r, but got %r' %
            (dct, key))
    return fun