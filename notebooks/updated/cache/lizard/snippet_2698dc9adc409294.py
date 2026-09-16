def timestamp(cls, name, description=None, unit='', default=None,
    initial_status=None):
    return cls(cls.TIMESTAMP, name, description, unit, None, default,
        initial_status)