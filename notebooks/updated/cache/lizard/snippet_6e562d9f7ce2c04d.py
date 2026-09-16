def to_bytes(x):
    if isinstance(x, bytes):
        return x
    if isinstance(x, basestring):
        return x.encode('utf-8')