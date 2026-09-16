def force_unicode(value):
    if not isinstance(value, (str, unicode)):
        value = unicode(value)
    if isinstance(value, str):
        value = value.decode('utf-8')
    return value