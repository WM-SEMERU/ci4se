def timestampFormat(self, timestampFormat):
    if not isinstance(timestampFormat, str):
        raise TypeError('not of type unicode')
    self._timestampFormat = timestampFormat