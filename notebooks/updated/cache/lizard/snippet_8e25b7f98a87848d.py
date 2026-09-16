def identifier(self):
    if self.primary_key not in self._data:
        return 'Unknown'
    return str(self._data[self.primary_key])