def get(self, name, default=None):
    try:
        return self._get(name, default)
    except KeyError:
        return default