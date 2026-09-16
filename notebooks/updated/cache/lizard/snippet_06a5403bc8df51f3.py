def text(self):
    if isinstance(self._value, CommentedMap):
        raise TypeError('{0} is a mapping, has no text value.'.format(repr(
            self)))
    if isinstance(self._value, CommentedSeq):
        raise TypeError('{0} is a sequence, has no text value.'.format(repr
            (self)))
    return self._text