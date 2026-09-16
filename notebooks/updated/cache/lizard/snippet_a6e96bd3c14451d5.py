def scan_model_keys(cls, count=None):
    pattern = cls.make_key(cls._name, '*')
    return cls.database.scan_keys(pattern, count)