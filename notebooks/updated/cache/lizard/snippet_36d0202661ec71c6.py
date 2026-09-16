def set(self, name, value, domain, **kwargs):
    if domain == 'localhost':
        domain = ''
    self.cookiejar.set_cookie(create_cookie(name, value, domain, **kwargs))