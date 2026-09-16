def get(self, key, default=None, cast=True):
    tablename, _, key = key.rpartition(':')
    if tablename and tablename not in self.fields.name.split('+'):
        raise ItsdbError('column requested from wrong table: {}'.format(
            tablename))
    try:
        index = self.fields.index(key)
        value = list.__getitem__(self, index)
    except (KeyError, IndexError):
        value = default
    else:
        if cast:
            field = self.fields[index]
            value = _cast_to_datatype(value, field)
    return value