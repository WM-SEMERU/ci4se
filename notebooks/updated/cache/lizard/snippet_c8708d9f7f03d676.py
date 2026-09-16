def _key_to_keyfunc(k):
    if isinstance(k, six.string_types):

        def lookup(x):
            return x[k]
        return lookup
    return k