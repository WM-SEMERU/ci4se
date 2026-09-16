def get_url(cls, data):
    try:
        data = int(data)
    except (ValueError, TypeError):
        pass
    if isinstance(data, int):
        return '%s%s%s' % (cls._url, cls.id_url, data)
    elif data is None:
        return cls._url
    elif isinstance(data, basestring):
        if '=' in data:
            key, value = data.split('=')
            if key in cls.search_types:
                return '%s%s%s' % (cls._url, cls.search_types[key], value)
            else:
                raise JSSUnsupportedSearchMethodError(
                    'This object cannot be queried by %s.' % key)
        else:
            return '%s%s%s' % (cls._url, cls.search_types[cls.
                default_search], data)
    else:
        raise ValueError