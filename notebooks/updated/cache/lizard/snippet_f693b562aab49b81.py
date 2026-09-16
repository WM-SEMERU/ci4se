def to_normal_url(cls, url):
    regexes = cls._get_url_scheme_regexes()
    _url = url[:]
    for scheme_key, pattern, regex in regexes:
        if _url.startswith(scheme_key):
            if '{1}' in pattern:
                _url = pattern.replace('{1}', _url.lstrip(scheme_key))
            else:
                _url = pattern + _url.lstrip(scheme_key).lstrip('://')
    return _url