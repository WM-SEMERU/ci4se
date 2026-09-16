def get_connection_cls(cls):
    if cls.__connection_cls is None:
        cls.__connection_cls, _ = cls.from_settings()
    return cls.__connection_cls