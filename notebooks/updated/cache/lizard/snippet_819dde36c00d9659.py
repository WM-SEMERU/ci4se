def to_utf8(x):
    if isinstance(x, basestring):
        return x.encode('utf-8') if isinstance(x, unicode) else x
    try:
        l = iter(x)
    except TypeError:
        return x
    return [to_utf8(i) for i in l]