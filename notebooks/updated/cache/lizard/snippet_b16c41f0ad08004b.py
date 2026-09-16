def from_dict(cls, fields, mapping):
    iterable = [None] * len(fields)
    for key, value in mapping.items():
        try:
            index = fields.index(key)
        except KeyError:
            raise ItsdbError('Invalid field name(s): ' + key)
        iterable[index] = value
    return cls(fields, iterable)