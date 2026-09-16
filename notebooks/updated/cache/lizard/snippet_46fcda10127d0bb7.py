def register(cls):
    if not issubclass(cls, Entity):
        raise ValueError(
            'Class must be a subclass of abilian.core.entities.Entity')
    SupportTagging.register(cls)
    return cls