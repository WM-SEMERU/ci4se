def _proxy(self):
    if self._context is None:
        self._context = CountryContext(self._version, iso_country=self.
            _solution['iso_country'])
    return self._context