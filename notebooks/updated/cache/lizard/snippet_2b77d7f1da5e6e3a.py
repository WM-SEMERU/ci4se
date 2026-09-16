def GetAttributeContainerByIndex(self, index):
    if index < 0:
        raise IndexError('Unsupported negative index value: {0:d}.'.format(
            index))
    if index < len(self._list):
        return self._list[index]
    return None