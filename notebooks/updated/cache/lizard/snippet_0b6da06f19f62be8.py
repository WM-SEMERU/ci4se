def fromExpiresIn(cls, expires_in, handle, secret, assoc_type):
    issued = int(time.time())
    lifetime = expires_in
    return cls(handle, secret, issued, lifetime, assoc_type)