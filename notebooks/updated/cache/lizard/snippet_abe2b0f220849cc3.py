def ensure_unicode(str_or_unicode):
    if isinstance(str_or_unicode, str):
        return str_or_unicode.decode('utf-8')
    elif isinstance(str_or_unicode, unicode):
        return str_or_unicode
    else:
        raise ValueError(
            "Input '{0}' should be a string or unicode, but its of type {1}"
            .format(str_or_unicode, type(str_or_unicode)))