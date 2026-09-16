def _error(self, message, start, end=None):
    raise errors.EfilterParseError(source=self.source, start=start, end=end,
        message=message)