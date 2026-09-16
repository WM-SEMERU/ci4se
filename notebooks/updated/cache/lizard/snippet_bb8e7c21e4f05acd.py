def has_data(self):
    if not hasattr(self, '_has_data'):
        try:
            next(iter(self.delegate.keys()))
            self._has_data = True
        except StopIteration:
            self._has_data = False
    return self._has_data