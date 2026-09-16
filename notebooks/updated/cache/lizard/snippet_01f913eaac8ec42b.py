def to_unicode_or_none(value):
    if value == ffi.NULL:
        return None
    elif isinstance(value, ffi.CData):
        return ffi.string(value).decode('utf-8')
    else:
        raise ValueError('Value must be char[] or NULL')