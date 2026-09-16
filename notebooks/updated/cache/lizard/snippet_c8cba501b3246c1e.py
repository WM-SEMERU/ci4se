def set_implementation(impl):
    global __impl__
    if impl.lower() == 'python':
        __impl__ = __IMPL_PYTHON__
    elif impl.lower() == 'c':
        __impl__ = __IMPL_C__
    else:
        import warnings
        warnings.warn('Implementation ' + impl +
            ' is not known. Using the fallback python implementation.')
        __impl__ = __IMPL_PYTHON__