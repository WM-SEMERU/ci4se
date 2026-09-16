def from_string(cls, s, space):
    import hashlib
    hs = hashlib.sha1(s).hexdigest()
    return cls.from_hex(hs, space)