def fetch(bank, key, cachedir=None):
    if cachedir is None:
        cachedir = __opts__['cachedir']
    try:
        cache = salt.cache.Cache(__opts__, cachedir=cachedir)
    except TypeError:
        cache = salt.cache.Cache(__opts__)
    return cache.fetch(bank, key)