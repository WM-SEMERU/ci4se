def assignIfExists(opts, default=None, **kwargs):
    for opt in opts:
        if opt in kwargs:
            return kwargs[opt]
    return default