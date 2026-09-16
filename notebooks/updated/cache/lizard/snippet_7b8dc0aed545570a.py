def has_name_in(cls, names):
    return cls.sha512.in_({cls.hash_name(name) for name in names})