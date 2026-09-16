def first(self):
    if not self._stream:
        raise InvalidUsage('first() is only available when stream=True')
    try:
        content = next(self.all())
    except StopIteration:
        raise NoResults('No records found')
    return content