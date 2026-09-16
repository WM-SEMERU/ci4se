def method_args(self, context, **kwargs):
    try:
        _args = self.conf[context].copy()
    except KeyError:
        _args = kwargs
    else:
        _args.update(kwargs)
    return _args