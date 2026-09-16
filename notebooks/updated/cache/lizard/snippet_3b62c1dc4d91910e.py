def heapify(self, key=__marker):
    if key is self.__marker:
        n = len(self._heap)
        for pos in reversed(range(n // 2)):
            self._sink(pos)
    else:
        try:
            pos = self._position[key]
        except KeyError:
            raise KeyError(key)
        self._reheapify(pos)