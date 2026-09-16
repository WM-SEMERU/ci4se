def make_good_url(url=None, addition='/'):
    if url is None:
        return None
    if isinstance(url, str) and isinstance(addition, str):
        return '%s/%s' % (url.rstrip('/'), addition.lstrip('/'))
    else:
        return None