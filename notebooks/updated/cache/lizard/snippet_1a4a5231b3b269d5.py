def data(self):
    if self._data is None:
        with open(self.path, 'rb') as f:
            self.read_data(f)
    return self._data