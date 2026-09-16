def _has_method(arg, method):
    return hasattr(arg, method) and callable(getattr(arg, method))