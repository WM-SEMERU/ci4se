def set_element(self, index, e):
    r
    if index > len(self._chain):
        raise IndexError(
            'tried to access element %i, but chain has only %i elements' %
            (index, len(self._chain)))
    if type(index) is not int:
        raise ValueError("index is not a integer but '%s'" % str(type(index)))
    if self._chain[index] is e:
        return
    replaced = self._chain.pop(index)
    if not replaced.is_reader:
        replaced.data_producer = None
    self._chain.insert(index, e)
    if index == 0:
        e.data_producer = e
    else:
        e.data_producer = self._chain[index - 1]
    try:
        successor = self._chain[index + 1]
        successor.data_producer = e
    except IndexError:
        pass
    self._chain[index]._estimated = False
    return replaced