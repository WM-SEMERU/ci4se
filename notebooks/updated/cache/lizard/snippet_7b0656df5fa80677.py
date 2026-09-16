def create_protocol(name, **kwargs):
    cls = protocol_map.get(name)
    if not cls:
        raise ValueError('Unsupported protocol "%s".' % name)
    return cls(**kwargs)