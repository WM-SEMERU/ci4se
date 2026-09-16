def from_(self, From):
    if self._type.lower() != 'edge':
        raise ValueError('Cannot set From/To to non-edge objects')
    self._from = From
    return self