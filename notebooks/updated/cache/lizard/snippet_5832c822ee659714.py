def peek(self, default=_marker):
    if not hasattr(self, '_peek'):
        try:
            self._peek = next(self._it)
        except StopIteration:
            if default is _marker:
                raise
            return default
    return self._peek