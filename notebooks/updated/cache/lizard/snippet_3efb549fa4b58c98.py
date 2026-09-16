def build_url(self, *args, **kwargs):
    parts = [kwargs.get('base_url') or self.base_url]
    parts.extend(args)
    parts = [str(p) for p in parts]
    key = tuple(parts)
    __logs__.info('Building a url from %s', key)
    if not key in __url_cache__:
        __logs__.info('Missed the cache building the url')
        __url_cache__[key] = '/'.join(parts)
    return __url_cache__[key]