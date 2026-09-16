def get_header(self, name, default=None):
    return self._handler.headers.get(name, default)