def _asciify_dict(data):
    ret = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = _remove_accents(key)
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = _remove_accents(value)
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _asciify_list(value)
        elif isinstance(value, dict):
            value = _asciify_dict(value)
        ret[key] = value
    return ret