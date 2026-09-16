def from_defaults(cls, **kwargs):
    options = TelluricContext.default_options()
    options.update(**kwargs)
    return cls(**options)