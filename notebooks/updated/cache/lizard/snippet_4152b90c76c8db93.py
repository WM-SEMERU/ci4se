def _validate_iterable(self, is_iterable, key, value):
    if is_iterable:
        try:
            iter(value)
        except TypeError:
            self._error(key, 'Must be iterable (e.g. a list or array)')