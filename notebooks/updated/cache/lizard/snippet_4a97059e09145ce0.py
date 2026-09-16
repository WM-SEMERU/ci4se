def items(self, start=None, stop=None):
    if start is None:
        node = self._head[2]
    else:
        self._find_lt(start)
        node = self._path[0][2]
    while node is not self._tail and (stop is None or node[0] < stop):
        yield node[0], node[1]
        node = node[2]