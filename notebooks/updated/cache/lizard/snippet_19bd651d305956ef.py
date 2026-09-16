def header(self, name, default=None):
    wsgi_header = 'HTTP_{0}'.format(name.upper())
    try:
        return self.env_raw[wsgi_header]
    except KeyError:
        return default