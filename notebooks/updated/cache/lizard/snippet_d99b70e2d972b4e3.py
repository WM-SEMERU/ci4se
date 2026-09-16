def get_cookie(self, key, secret=None):
    value = self.COOKIES.get(key)
    if secret and value:
        dec = cookie_decode(value, secret)
        return dec[1] if dec and dec[0] == key else None
    return value or None