def validate(opts):
    if hasattr(opts, 'extensions'):
        return _validate(opts.extensions)
    elif isinstance(opts, list):
        return _validate(opts)
    else:
        raise ValueError(
            "Value passed into extension validation must either be a list of strings or a namespace with an attribute of 'extensions'"
            )