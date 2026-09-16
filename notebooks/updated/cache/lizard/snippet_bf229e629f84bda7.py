def looks_like_url(url):
    if not isinstance(url, basestring):
        return False
    if not isinstance(url, basestring) or len(url
        ) >= 1024 or not cre_url.match(url):
        return False
    return True