def copy(self):
    return self.__class__(self, key=self._key, load=self._load)