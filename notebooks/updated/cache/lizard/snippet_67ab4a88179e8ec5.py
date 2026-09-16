def path(self, value=None):
    if value is not None:
        if not value.startswith('/'):
            value = '/' + value
        encoded_value = unicode_quote(value)
        return URL._mutate(self, path=encoded_value)
    return self._tuple.path