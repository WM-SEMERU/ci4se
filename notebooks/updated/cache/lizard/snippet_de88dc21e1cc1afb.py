def _fixIndex(self, index, truncate=False):
    assert not isinstance(index, slice), 'slices are not supported (yet)'
    if index < 0:
        index += self.length
    if index < 0:
        if not truncate:
            raise IndexError('stored List index out of range')
        else:
            index = 0
    return index