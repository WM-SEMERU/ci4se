def copy(self):
    copied = ColorVisuals()
    copied._data.data = copy.deepcopy(self._data.data)
    return copied