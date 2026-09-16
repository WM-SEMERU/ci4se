def _handle_result_by_key(self, key):
    invalid_options = 'key', 'keys', 'startkey', 'endkey'
    if any(x in invalid_options for x in self.options):
        raise ResultException(102, invalid_options, self.options)
    return self._ref(key=key, **self.options)