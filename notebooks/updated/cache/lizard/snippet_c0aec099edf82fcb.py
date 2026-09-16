def keys(self):
    keys = self._keys
    if keys is None:
        keys = tuple(self[i].name for i in self.key_indices)
    return keys