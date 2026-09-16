def rewind(self, position=0):
    if position < 0 or position > len(self._data):
        raise Exception('Invalid position to rewind cursor to: %s.' % position)
    self._position = position