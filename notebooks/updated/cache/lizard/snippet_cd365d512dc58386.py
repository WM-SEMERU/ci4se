def from_httplib(cls, message, duplicates=('set-cookie',)):
    ret = cls(message.items())
    for key in duplicates:
        ret.discard(key)
        for val in message.getheaders(key):
            ret.add(key, val)
        return ret