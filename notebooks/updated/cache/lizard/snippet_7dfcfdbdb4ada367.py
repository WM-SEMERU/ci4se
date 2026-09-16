def remove_data_point(self, x, y):
    if len(self._data) == 1:
        raise ValueError("You cannot remove a Series' last data point")
    self._data.remove((x, y))