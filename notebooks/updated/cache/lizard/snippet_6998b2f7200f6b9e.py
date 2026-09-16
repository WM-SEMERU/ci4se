def encode(value, encoding='utf-8', encoding_errors='strict'):
    if isinstance(value, bytes):
        return value
    if not isinstance(value, basestring):
        value = str(value)
    if isinstance(value, unicode):
        value = value.encode(encoding, encoding_errors)
    return value