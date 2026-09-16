def get_size(cls):
    return sum([getattr(cls, name).length for name in cls.get_fields_names()])