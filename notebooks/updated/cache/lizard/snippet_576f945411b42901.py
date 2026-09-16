def _get_column(cls, name):
    if name == 'pk':
        return cls._meta.get_field(cls._meta.pk.name)
    return cls._columns[name]