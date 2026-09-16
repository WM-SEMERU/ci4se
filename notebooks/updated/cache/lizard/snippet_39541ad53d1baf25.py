def encode_cookie(payload, key=None):
    return '{0}|{1}'.format(payload, _cookie_digest(payload, key=key))