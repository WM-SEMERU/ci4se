def add_cookie(self, key, value, **attrs):
    if attrs:
        c = Morsel()
        c.set(key, value, **attrs)
        self.cookies[key] = c
    else:
        self.cookies[key] = value