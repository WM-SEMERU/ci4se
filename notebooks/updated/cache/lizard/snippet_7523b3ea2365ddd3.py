def getLogger(name=None, filename=None, filemode=None, level=WARNING):
    warnings.warn('getLogger is deprecated, Use get_logger instead.',
        DeprecationWarning, stacklevel=2)
    return get_logger(name, filename, filemode, level)