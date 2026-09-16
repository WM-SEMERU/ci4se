def from_dict(config_cls, dictionary, validate=False):
    return _build(config_cls, dictionary, validate=validate)