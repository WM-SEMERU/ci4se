def _detect_encoding(self, source_file):
    encoding = self._guess(source_file)
    if encoding is None:
        encoding = self.default_encoding
    return encoding