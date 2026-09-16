def prepare(cls, value):
    pfield = struct.pack('b', cls.type_code)
    if isinstance(value, string_types):
        value = datetime.datetime.strptime(value, '%Y-%m-%d')
    year = value.year | 32768
    month = value.month - 1
    pfield += cls._struct.pack(year, month, value.day)
    return pfield