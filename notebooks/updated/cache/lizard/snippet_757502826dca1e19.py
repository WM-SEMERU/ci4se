def register_type(klass, type_url=None):
    if type_url is None:
        type_url = _compute_type_url(klass)
    if type_url in _TYPE_URL_MAP:
        if _TYPE_URL_MAP[type_url] is not klass:
            raise ValueError('Conflict: %s' % (_TYPE_URL_MAP[type_url],))
    _TYPE_URL_MAP[type_url] = klass