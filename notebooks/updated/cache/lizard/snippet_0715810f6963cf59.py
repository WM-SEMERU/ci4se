def from_config(cls, config, prefix='postmark_', is_uppercase=False):
    kwargs = {}
    for arg in get_args(cls):
        key = prefix + arg
        if is_uppercase:
            key = key.upper()
        else:
            key = key.lower()
        if key in config:
            kwargs[arg] = config[key]
    return cls(**kwargs)