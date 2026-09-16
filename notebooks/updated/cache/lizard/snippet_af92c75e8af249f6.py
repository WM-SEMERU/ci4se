def is_callable(self):
    if not callable(self._subject):
        raise self._error_factory(_format('Expected {} to be callable',
            self._subject))