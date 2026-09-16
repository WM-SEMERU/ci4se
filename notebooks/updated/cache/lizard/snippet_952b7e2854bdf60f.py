def description(self, value):
    try:
        value = np.dtype(value)
    except TypeError as e:
        return None
    for dtype, string in self._all:
        if dtype == value:
            return string
    return None