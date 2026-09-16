def _instantiate(cls, params):
    sig_params = inspect.signature(cls.__init__).parameters
    valid_params = dict()
    for key, value in params.items():
        if key in sig_params:
            valid_params[key] = value
        else:
            logger.debug("Type %s does not support parameter '%s'" % (cls.
                __name__, key))
    return cls(**valid_params)