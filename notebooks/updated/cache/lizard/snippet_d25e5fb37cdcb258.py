def _get_param_names(cls):
    init = getattr(cls.__init__, 'deprecated_original', cls.__init__)
    if init is object.__init__:
        return []
    args, varargs, kw, default = getargspec_no_self(init)
    if varargs is not None:
        raise RuntimeError(
            "scikit-learn estimators should always specify their parameters in the signature of their __init__ (no varargs). %s doesn't follow this convention."
             % (cls,))
    args.sort()
    return args